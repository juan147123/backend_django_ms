from rest_framework import serializers
from .models import RiesgosOportunidadesEncabezado


class RiesgosOportunidadesEncabezadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiesgosOportunidadesEncabezado
        fields = '__all__'  
