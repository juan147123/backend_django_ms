# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CentroGestion(models.Model):
    cg_code = models.CharField(max_length=255, blank=True, null=True)  
    cg_name = models.CharField(max_length=255, blank=True, null=True)  
    cg_pais = models.CharField(max_length=2, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    cg_tipo_nodo = models.CharField(max_length=255, blank=True, null=True)  
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cg_estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centro_gestion'
