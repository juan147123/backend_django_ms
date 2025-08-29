from rest_framework import serializers

from controles.serializer import ControlesSerializer
from eficacia.serializer import EficaciaReadSerializer
from evaluacion.serializer import EvaluacionReadSerializer
from tratamiento.serializer import TratamientoReadSerializer
from .models import RiesgosOportunidades
from mantenimientos.models import Mantenimientos
from mantenimientos.serializer import MantenimientosSerializer


class RiesgosOportunidadesReadSerializer(serializers.ModelSerializer):
    # Usamos el serializador de Mantenimientos para anidar los datos
    id_amenaza_oportunidad = MantenimientosSerializer()
    id_proceso = MantenimientosSerializer()
    id_tipo_riesgo = MantenimientosSerializer()
    id_sistema_gestion = MantenimientosSerializer()
    id_fortaleza_debilidad = MantenimientosSerializer()
    controles = serializers.SerializerMethodField()  # Método para obtener controles
    evaluaciones = serializers.SerializerMethodField()  # Método para obtener controles
    tratamientos = serializers.SerializerMethodField()  # Método para obtener controles
    eficacias = serializers.SerializerMethodField()  # Método para obtener controles

    class Meta:
        model = RiesgosOportunidades
        fields = '__all__'

    def get_controles(self, obj):
        return ControlesSerializer(obj.get_controles(), many=True).data

    def get_evaluaciones(self, obj):
        return EvaluacionReadSerializer(obj.get_evaluaciones(), many=True).data

    def get_tratamientos(self, obj):
        return TratamientoReadSerializer(obj.get_tratamientos(), many=True).data

    def get_eficacias(self, obj):
        return EficaciaReadSerializer(obj.get_eficacias(), many=True).data


class RiesgosOportunidadesWriteSerializer(serializers.ModelSerializer):
    id_amenaza_oportunidad = serializers.PrimaryKeyRelatedField(
        queryset=Mantenimientos.objects.all(), allow_null=True, required=False
    )
    id_fortaleza_debilidad = serializers.PrimaryKeyRelatedField(
        queryset=Mantenimientos.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = RiesgosOportunidades
        fields = '__all__'

    def create(self, validated_data):
        # Obtener el tipo de riesgo y id_encabezado
        tipo_riesgo = validated_data.get('tipo_riesgo', '')
        id_encabezado = validated_data.get('id_encabezado')
        cod_riesgo_enviado = validated_data.get('cod_riesgo', '')
        
        # Si se envió un código específico, usarlo como prefijo
        if cod_riesgo_enviado and cod_riesgo_enviado.strip():
            # Si es "R" o "O", usarlo como prefijo
            if cod_riesgo_enviado.upper() in ['R', 'O']:
                prefijo = cod_riesgo_enviado.upper()
            else:
                # Si es otro código, usarlo tal como está
                validated_data['cod_riesgo'] = cod_riesgo_enviado
                return super().create(validated_data)
        else:
            # Si no se envió código, determinar el prefijo basado en el tipo
            if tipo_riesgo.upper() == 'R':
                prefijo = 'R'
            elif tipo_riesgo.upper() == 'O':
                prefijo = 'O'
            else:
                # Si no es R u O, usar el tipo como está
                prefijo = tipo_riesgo.upper()
        
        # Generar el código automáticamente
        if id_encabezado is not None:
            # Contar cuántos registros existen con el mismo id_encabezado y tipo
            count = RiesgosOportunidades.objects.filter(
                id_encabezado=id_encabezado,
                tipo_riesgo=tipo_riesgo,
                enable=1
            ).count()
            
            # El nuevo código será prefijo + "-" + (count + 1)
            nuevo_codigo = f"{prefijo}-{count + 1}"
        else:
            # Si no hay id_encabezado, generar un código simple
            count = RiesgosOportunidades.objects.filter(
                tipo_riesgo=tipo_riesgo,
                enable=1
            ).count()
            nuevo_codigo = f"{prefijo}-{count + 1}"
        
        # Asignar el código generado
        validated_data['cod_riesgo'] = nuevo_codigo
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Al actualizar, mantener el código original sin generar uno nuevo
        # Solo se genera código automáticamente en la creación
        return super().update(instance, validated_data)
