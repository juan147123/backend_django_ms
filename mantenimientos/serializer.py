from rest_framework import serializers
from .models import Mantenimientos


class MantenimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimientos
        fields = ('id', 'codigo', 'categoria', 'descripcion','enable')
        read_only_fields = ('created_at', 'updated_at', )
