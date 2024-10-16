from django.db import models


class SapMaestroRutBi(models.Model):
    rut = models.CharField(max_length=20, primary_key=True)
    razon_social = models.CharField(max_length=100, null=True, blank=True)
    base = models.CharField(max_length=100, null=True, blank=True)
    clave = models.TextField(null=True, blank=True)
    ruta_portal_prov = models.CharField(max_length=100, null=True, blank=True)
    ruta_web_req = models.CharField(max_length=100, null=True, blank=True)
    base_vigente = models.CharField(max_length=50, null=True, blank=True)
    grupo_hologacion = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = '"legal"."sap_maestro_rut_bi"'


class VwCecoConsolidadoGF(models.Model):
    id_unidad_negocio = models.CharField(max_length=50,primary_key=True)
    unidad_negocio_desc = models.CharField(max_length=255)
    codigo_centro_gestion = models.CharField(max_length=50)
    centro_gestion_desc = models.CharField(max_length=255)
    ruc_empresa = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=255)
    id_unidad_negocio_sap = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    cod_empresa = models.CharField(max_length=50)
    base_vigente_empresa = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = '"ggo"."vw_ceco_consolidado_gf"'
