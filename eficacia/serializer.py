from rest_framework import serializers

from mantenimientos.serializer import MantenimientosSerializer
from .models import Eficacia


class EficaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eficacia
        fields = '__all__'  

class EficaciaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eficacia
        fields = '__all__'  
