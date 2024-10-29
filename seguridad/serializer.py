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



#seguridad app - autenticacion



class RolAplicacionAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolAplicacion
        fields = ('id_rol','nombre',)  
class UsuarioRolAuthSerializer(serializers.ModelSerializer):
    id_rol = RolAplicacionAuthSerializer() 
    class Meta:
        model = UsuarioRol
        fields = ('objeto_permitido','pais','id_rol',)
class AplicacionUsuarioAuthSerializer(serializers.ModelSerializer):
    usuariorol_set = UsuarioRolAuthSerializer(many=True, read_only=True)
    class Meta:
        model = AplicacionUsuario
        fields = ('username','usuariorol_set',)
