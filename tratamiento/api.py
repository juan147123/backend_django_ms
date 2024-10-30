from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tratamiento
from .serializer import TratamientoReadSerializer, TratamientoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class TratamientoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["id_riesgo_oportunidad","enable"]
    serializer_class = TratamientoSerializer 
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = Tratamiento.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TratamientoReadSerializer
        return TratamientoSerializer  

    @action(detail=False, methods=['delete'], url_path='logical/delete/(?P<id>[^/.]+)')
    def logical_delete(self,request, id=None):
        try:
            registro = Tratamiento.objects.get(id=id)
            registro.enable = 0
            registro.save()
            return Response({'delete': 1})
        except Tratamiento.DoesNotExist:
            return Response({'error': 'registro no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:  
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)