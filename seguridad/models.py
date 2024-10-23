from django.db import models
class AplicacionUsuario(models.Model):
    id_aplicacion_usuario = models.BigAutoField(primary_key=True)
    id_aplicacion = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    provider_id = models.CharField(max_length=255, blank=True, null=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=1024, blank=True, null=True)
    fecha_ini = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'aplicacion_usuario'




class RolAplicacion(models.Model):
    id_rol = models.AutoField(primary_key=True)
    id_aplicacion = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol_aplicacion'


class UsuarioRol(models.Model):
    id_usuario_rol = models.BigAutoField(primary_key=True)
    id_aplicacion_usuario = models.ForeignKey(AplicacionUsuario, models.DO_NOTHING, db_column='id_aplicacion_usuario')
    id_rol = models.IntegerField()
    objeto_permitido = models.CharField(max_length=5120, blank=True, null=True)
    pais = models.CharField(max_length=10, blank=True, null=True)
    estado = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'usuario_rol'
