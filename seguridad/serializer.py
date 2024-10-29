from rest_framework import serializers

from centrogestion.models import CentroGestion
from .models import AplicacionUsuario, RolAplicacion, UsuarioRol


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


# seguridad app - autenticacion


class RolAplicacionAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolAplicacion
        fields = ('id_rol', 'nombre',)

class UsuarioRolAuthSerializer(serializers.ModelSerializer):
    id_rol = RolAplicacionAuthSerializer()
    objeto_permitido_descripcion = serializers.SerializerMethodField()

    class Meta:
        model = UsuarioRol
        fields = ('objeto_permitido', 'objeto_permitido_descripcion', 'pais', 'id_rol',)

    def get_objeto_permitido_descripcion(self, obj):
        centro_gestion = CentroGestion.objects.filter(id=obj.objeto_permitido).first()
        return centro_gestion.label if centro_gestion else None


class AplicacionUsuarioAuthSerializer(serializers.ModelSerializer):
    usuariorol_set = UsuarioRolAuthSerializer(many=True, read_only=True)

    class Meta:
        model = AplicacionUsuario
        fields = ('username', 'name', 'usuariorol_set',)