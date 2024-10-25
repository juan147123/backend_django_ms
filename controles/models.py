from django.db import models

from riesgosoportunidades.models import RiesgosOportunidades


class Controles(models.Model):
    id_riesgo_oportunidad = models.ForeignKey(
        RiesgosOportunidades, models.DO_NOTHING, db_column='id_riesgo_oportunidad')
    nro_grado_aplicacion = models.IntegerField()
    des_grado_aplicacion = models.CharField(max_length=255)
    nro_definicion_responsables = models.IntegerField()
    des_definicion_responsables = models.CharField(max_length=255)
    nro_grado_evidencia = models.IntegerField()
    des_grado_evidencia = models.CharField(max_length=255)
    nro_calculo_nivel_eficacia = nro_calculo_nivel_eficacia = models.DecimalField(
        max_digits=5,
        decimal_places=1,
    )
    des_calculo_nivel_eficacia = models.CharField(max_length=255)
    efectividad_control = models.CharField(max_length=255)
    enable = models.IntegerField(default=1)
    controles_existentes = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'controles'
