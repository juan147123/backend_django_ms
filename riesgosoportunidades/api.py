from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import RiesgosOportunidades
from .serializer import RiesgosOportunidadesReadSerializer, RiesgosOportunidadesWriteSerializer


class RiesgosOportunidadesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["tipo_riesgo", "enable", "id_cege"]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = RiesgosOportunidades.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return RiesgosOportunidadesReadSerializer
        return RiesgosOportunidadesWriteSerializer
