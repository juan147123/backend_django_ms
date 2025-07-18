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
