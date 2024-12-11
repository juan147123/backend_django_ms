from django.db import models
from mantenimientos.models import Mantenimientos

class RiesgosOportunidades(models.Model):
    id_encabezado = models.IntegerField(blank=True, null=True)
    cod_riesgo = models.CharField(max_length=255)
    tipo_riesgo = models.CharField(max_length=255)
    id_proceso =  models.ForeignKey(
        Mantenimientos, models.DO_NOTHING, db_column='id_proceso', related_name='riesgosoportunidades_id_proceso_set')
    descripcion = models.TextField()
    id_partes_externas = models.TextField(blank=True, null=True) 
    id_amenaza_oportunidad = models.ForeignKey(
        Mantenimientos, models.DO_NOTHING, db_column='id_amenaza_oportunidad', related_name='riesgosoportunidades_id_amenaza_oportunidad_set')
    id_fortaleza_debilidad = models.ForeignKey(
        Mantenimientos, models.DO_NOTHING, db_column='id_fortaleza_debilidad', related_name='riesgosoportunidades_id_fortaleza_debilidad_set')
    enable = models.IntegerField(default=1)
    id_cege = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'riesgos_oportunidades'

    def get_controles(self):
        from controles.models import Controles 
        return Controles.objects.filter(id_riesgo_oportunidad=self,enable=1)

    def get_evaluaciones(self):
        from evaluacion.models import Evaluacion 
        return Evaluacion.objects.filter(id_riesgo_oportunidad=self,enable=1)

    def get_tratamientos(self):
        from tratamiento.models import Tratamiento 
        return Tratamiento.objects.filter(id_riesgo_oportunidad=self,enable=1)
    
    def get_eficacias(self):
        from eficacia.models import Eficacia 
        return Eficacia.objects.filter(id_riesgo_oportunidad=self,enable=1)