from django.db import models

from riesgosoportunidades.models import RiesgosOportunidades

class Eficacia(models.Model):
    fecha_evaluacion = models.DateField()
    eficaz = models.BooleanField(blank=True, null=True)
    justificacion = models.TextField()
    evidencia = models.CharField(max_length=550)
    enable = models.IntegerField(default=1)
    id_riesgo_oportunidad = models.ForeignKey(RiesgosOportunidades, models.DO_NOTHING, db_column='id_riesgo_oportunidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eficacia'