from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import RiesgosOportunidadesEncabezado
from .serializer import RiesgosOportunidadesEncabezadoSerializer


class RiesgosOportunidadesEncabezadoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["anio","id_cege","enable"]
    serializer_class = RiesgosOportunidadesEncabezadoSerializer 
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = RiesgosOportunidadesEncabezado.objects.all()