from django.db import models

from riesgos.models import RiesgosOportunidades


class Controles(models.Model):
    id_riesgo_oportunidad = models.ForeignKey(
        RiesgosOportunidades, models.DO_NOTHING, db_column='id_riesgo_oportunidad')
    nro_grado_aplicacion = models.IntegerField(null=True, blank=True)
    des_grado_aplicacion = models.CharField(
        max_length=255, null=True, blank=True)
    nro_definicion_responsables = models.IntegerField(null=True, blank=True)
    des_definicion_responsables = models.CharField(
        max_length=255, null=True, blank=True)
    nro_grado_evidencia = models.IntegerField(null=True, blank=True)
    des_grado_evidencia = models.CharField(
        max_length=255, null=True, blank=True)
    nro_calculo_nivel_eficacia = nro_calculo_nivel_eficacia = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True, blank=True
    )
    des_calculo_nivel_eficacia = models.CharField(
        max_length=255, null=True, blank=True)
    efectividad_control = models.CharField(
        max_length=255, null=True, blank=True)
    enable = models.IntegerField(default=1)
    controles_existentes = models.CharField(
        max_length=255, null=True, blank=True)
    probabilidad_oportunidad = models.IntegerField(null=True, blank=True)
    impacto_oportunidad = models.IntegerField(null=True, blank=True)
    nivel_oportunidad = models.IntegerField(null=True, blank=True)
    des_nivel_oportunidad = models.CharField(
        max_length=255, null=True, blank=True)
    des_probabilidad_oportunidad = models.CharField(
        max_length=255, null=True, blank=True)
    des_impacto_oportunidad = models.CharField(
        max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'controles'
