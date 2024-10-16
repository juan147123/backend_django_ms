from rest_framework import serializers
from .models import SapMaestroRutBi, VwCecoConsolidadoGF


class SapMaestroRutBiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SapMaestroRutBi
        fields = ('rut', 'razon_social', 'base', 'clave', 'ruta_portal_prov',
                  'ruta_web_req', 'base_vigente', 'grupo_hologacion')


class VwCecoConsolidadoGFSerializer(serializers.ModelSerializer):
    class Meta:
        model = VwCecoConsolidadoGF
        fields = [
            'id_unidad_negocio',
            'unidad_negocio_desc',
            'codigo_centro_gestion',
            'centro_gestion_desc',
            'ruc_empresa',
            'razon_social',
            'id_unidad_negocio_sap',
            'origen',
            'cod_empresa',
            'base_vigente_empresa'
        ]


class UnidadesGFSerializer(serializers.ModelSerializer):
    class Meta:
        model = VwCecoConsolidadoGF
        fields = [
            'id_unidad_negocio',
            'unidad_negocio_desc'
        ]

class CecosGFSerializer(serializers.ModelSerializer):
    class Meta:
        model = VwCecoConsolidadoGF
        fields = [
            'codigo_centro_gestion',
            'centro_gestion_desc'
        ]
