from rest_framework import serializers

from mantenimientos.serializer import MantenimientosSerializer
from .models import Tratamiento


class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'


class TratamientoReadSerializer(serializers.ModelSerializer):
    tipo_estrategia = MantenimientosSerializer(
        source='id_estrategia_tratamiento')
    tipo_estado = MantenimientosSerializer(source='id_estado')

    class Meta:
        model = Tratamiento
        fields = '__all__'


class TratamientoEstadoCumplimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ['estado_cumplimiento']
        
    def validate_estado_cumplimiento(self, value):
        if value not in ['pendiente', 'cumplido']:
            raise serializers.ValidationError("El estado debe ser 'pendiente' o 'cumplido'")
        return value
