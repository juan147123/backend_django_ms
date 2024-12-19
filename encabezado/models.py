from django.db import models

from centrogestion.models import CentroGestion

class RiesgosOportunidadesEncabezado(models.Model):
    anio = models.CharField(max_length=255, blank=True, null=True)
    id_cege = models.ForeignKey(CentroGestion, models.DO_NOTHING, db_column='id_cege', blank=True, null=True,  related_name='riesgosoportunidadesencabezado')
    enable = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'riesgos_oportunidades_encabezado'