from django.db import models

# Create your models here.


class Mantenimientos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50,null=True)
    categoria = models.CharField(max_length=100,null=True)
    enable = models.IntegerField(default=1)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
       
    class Meta:
        managed = False
        db_table = 'maintenance'