from rest_framework import serializers
from .models import CentroGestion


class CentroGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroGestion
        fields = ('id', 'cg_code', 'label', 'cg_pais', 'parent',
                  'cg_tipo_nodo', 'enable', 'ruc_empresa')
        read_only_fields = ('created_at', 'updated_at', )
