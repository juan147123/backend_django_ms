from rest_framework import serializers
from .models import Controles


class ControlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controles
        fields = '__all__'  
