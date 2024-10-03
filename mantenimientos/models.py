from django.db import models

# Create your models here.


class Mantenimientos(models.Model):
    codigo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    enable = models.IntegerField(default=1)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
       
    class Meta:
        managed = False
        db_table = 'maintenance'