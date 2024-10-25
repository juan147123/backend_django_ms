from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Controles
from .serializer import ControlesSerializer


class ControlesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["id_riesgo_oportunidad","enable"]
    serializer_class = ControlesSerializer 
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = Controles.objects.all()