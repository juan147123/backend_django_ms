from django.db import models


class CentroGestion(models.Model):
    cg_code = models.CharField(max_length=255, blank=True, null=True)  
    label = models.CharField(max_length=255, blank=True, null=True)  
    cg_pais = models.CharField(max_length=2, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    cg_tipo_nodo = models.CharField(max_length=255, blank=True, null=True)  
    ruc_empresa = models.CharField(max_length=255, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    enable = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'centro_gestion'
