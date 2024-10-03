from rest_framework import serializers
from .models import CentroGestion

class CentroGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroGestion
        fields = ('id', 'cg_code', 'cg_name', 'cg_pais', 'parent', 'cg_tipo_nodo', 'cg_estado')
        read_only_fields = ('created_at', 'updated_at', )
