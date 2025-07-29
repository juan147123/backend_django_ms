from django.db import models
from mantenimientos.models import Mantenimientos
from riesgos.models import RiesgosOportunidades

class Tratamiento(models.Model):
    ESTADO_CUMPLIMIENTO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('cumplido', 'Cumplido'),
    ]
    
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
    estado_cumplimiento = models.CharField(
        max_length=20,
        choices=ESTADO_CUMPLIMIENTO_CHOICES,
        default='pendiente'
    )
    
    class Meta:
        managed = False
        db_table = 'tratamiento'
