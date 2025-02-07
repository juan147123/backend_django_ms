from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import RiesgosOportunidades
from .serializer import RiesgosOportunidadesReadSerializer, RiesgosOportunidadesWriteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class RiesgosOportunidadesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["tipo_riesgo", "enable", "id_cege","id_encabezado"]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = RiesgosOportunidades.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return RiesgosOportunidadesReadSerializer
        return RiesgosOportunidadesWriteSerializer

    @action(detail=False, methods=['delete'], url_path='logical/delete/(?P<id>[^/.]+)')
    def logical_delete(self,request, id=None):
        try:
            registro = RiesgosOportunidades.objects.get(id=id)
            registro.enable = 0
            registro.save()
            return Response({'delete': 1})
        except RiesgosOportunidades.DoesNotExist:
            return Response({'error': 'registro no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:  
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)