from rest_framework import serializers
from centrogestion.models import CentroGestion

class CentroGestionDashboardSerializer(serializers.ModelSerializer):
    riesgos_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = CentroGestion
        fields = ('id', 'cg_code', 'label', 'cg_pais', 'parent',
                  'cg_tipo_nodo', 'enable', 'ruc_empresa','riesgos_count')
        read_only_fields = ('created_at', 'updated_at', )


class PieDashboardSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='riesgos_count', read_only=True)
    name = serializers.CharField(source='label', read_only=True)  

    class Meta:
        model = CentroGestion
        fields = ('value', 'name')
