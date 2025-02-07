from django.db import models
from mantenimientos.models import Mantenimientos
from riesgos.models import RiesgosOportunidades

class Tratamiento(models.Model):
    id_estrategia_tratamiento = models.ForeignKey(
        Mantenimientos,
        models.DO_NOTHING,
        db_column='id_estrategia_tratamiento',
        related_name='tratamientos_estrategia'  
    )
    actividades = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.TextField()
    recursos = models.TextField()
    id_estado = models.ForeignKey(
        Mantenimientos,
        models.DO_NOTHING,
        db_column='id_estado',
        related_name='tratamientos_estado'  
    )
    observaciones = models.TextField(blank=True, null=True)
    id_riesgo_oportunidad = models.ForeignKey(RiesgosOportunidades, models.DO_NOTHING, db_column='id_riesgo_oportunidad', blank=True, null=True)
    enable = models.IntegerField(default=1)
    class Meta:
        managed = False
        db_table = 'tratamiento'
