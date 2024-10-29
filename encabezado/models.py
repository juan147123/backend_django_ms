from django.db import models

class RiesgosOportunidadesEncabezado(models.Model):
    anio = models.CharField(max_length=255, blank=True, null=True)
    id_cege = models.IntegerField(blank=True, null=True)
    enable = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'riesgos_oportunidades_encabezado'