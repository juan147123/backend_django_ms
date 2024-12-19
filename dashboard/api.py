from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from centrogestion.models import CentroGestion
from .serializer import CentroGestionDashboardSerializer, PieDashboardSerializer
from rest_framework.decorators import action
from django.db.models import Count, Q

class CentroGestionDashboardViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CentroGestionDashboardSerializer
    queryset = CentroGestion.objects.all()


    
    @action(detail=False, methods=['get'], url_path='pie')
    def activos(self, request):
        try:
            # Contar los riesgos con enable=1 y filtrar solo aquellos con riesgos_count > 0
            data = CentroGestion.objects.annotate(
                riesgos_count=Count(
                    'riesgosoportunidadesencabezado__riesgosoportunidades',
                    filter=Q(riesgosoportunidadesencabezado__riesgosoportunidades__enable=1),
                    distinct=True
                )
            ).filter(riesgos_count__gt=0)  # Solo traer los registros donde el conteo es mayor que 0

            # Serializar los datos
            serializer = PieDashboardSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)