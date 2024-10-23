from rest_framework import serializers
from .models import  AplicacionUsuario, RolAplicacion, UsuarioRol

class AplicacionUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AplicacionUsuario
        fields = '__all__'

class RolAplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolAplicacion
        fields = '__all__'  


class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = '__all__'  
