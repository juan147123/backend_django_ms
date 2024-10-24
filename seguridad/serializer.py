from rest_framework import serializers
from .models import  AplicacionUsuario, RolAplicacion, UsuarioRol



class RolAplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolAplicacion
        fields = '__all__'  


class UsuarioRolSerializer(serializers.ModelSerializer):
    id_rol = RolAplicacionSerializer() 
    class Meta:
        model = UsuarioRol
        fields = '__all__'  

class AplicacionUsuarioSerializer(serializers.ModelSerializer):
    usuariorol_set = UsuarioRolSerializer(many=True, read_only=True)
    class Meta:
        model = AplicacionUsuario
        fields = '__all__'