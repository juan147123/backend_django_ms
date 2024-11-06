from rest_framework import serializers

from mantenimientos.serializer import MantenimientosSerializer
from .models import Evaluacion


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'  

class EvaluacionReadSerializer(serializers.ModelSerializer):
    tipo_riesgo = MantenimientosSerializer(source='id_tipo_riesgo')
    class Meta:
        model = Evaluacion
        fields = '__all__'  
