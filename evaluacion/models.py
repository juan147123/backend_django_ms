from django.db import models

from mantenimientos.models import Mantenimientos
from riesgos.models import RiesgosOportunidades

class Evaluacion(models.Model):
    nro_calculo_nivel_eficacia = models.DecimalField(max_digits=4, decimal_places=2)
    nro_probabilidad = models.IntegerField()
    nro_impacto = models.IntegerField()
    nro_calculo_nivel_riesgo = models.DecimalField(max_digits=4, decimal_places=2)
    des_calculo_nivel_riesgo = models.CharField(max_length=50)
    accion_tomar = models.TextField()
    id_tipo_riesgo = models.ForeignKey(Mantenimientos, models.DO_NOTHING, db_column='id_tipo_riesgo',null=True, blank=True)
    enable = models.IntegerField(default=1)
    id_riesgo_oportunidad = models.ForeignKey(RiesgosOportunidades, models.DO_NOTHING, db_column='id_riesgo_oportunidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluacion'

