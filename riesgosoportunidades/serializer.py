from rest_framework import serializers

from controles.serializer import ControlesSerializer
from .models import RiesgosOportunidades
from mantenimientos.models import Mantenimientos
from mantenimientos.serializer import MantenimientosSerializer

class RiesgosOportunidadesReadSerializer(serializers.ModelSerializer):
    # Usamos el serializador de Mantenimientos para anidar los datos
    id_partes_externas = MantenimientosSerializer()
    id_amenaza_oportunidad = MantenimientosSerializer()
    id_fortaleza_debilidad = MantenimientosSerializer()
    controles = serializers.SerializerMethodField()  # Método para obtener controles
    
    class Meta:
        model = RiesgosOportunidades
        fields = '__all__'

    def get_controles(self, obj):
        return ControlesSerializer(obj.get_controles(), many=True).data

class RiesgosOportunidadesWriteSerializer(serializers.ModelSerializer):
    # Usamos PrimaryKeyRelatedField para solo recibir los IDs
    id_partes_externas = serializers.PrimaryKeyRelatedField(queryset=Mantenimientos.objects.all())
    id_amenaza_oportunidad = serializers.PrimaryKeyRelatedField(queryset=Mantenimientos.objects.all())
    id_fortaleza_debilidad = serializers.PrimaryKeyRelatedField(queryset=Mantenimientos.objects.all())
    
    class Meta:
        model = RiesgosOportunidades
        fields = '__all__'
