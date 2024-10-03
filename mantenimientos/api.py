from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from .models import Mantenimientos
from .serializer import MantenimientosSerializer
from rest_framework.decorators import action


class MantenimientosViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = MantenimientosSerializer
    queryset = Mantenimientos.objects.all()

    @action(detail=False, methods=['get'], url_path='categoria/(?P<categoria>[^/.]+)')
    def categoria(self, request, categoria=None):
        try:
            mantenimientos = Mantenimientos.objects.filter(categoria=categoria, enable=1)
            serializer = self.get_serializer(mantenimientos, many=True)
            return Response(serializer.data)
        except Exception as e:
             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

   
    @action(detail=False, methods=['get'], url_path='activos')
    def activos(self, request,  categoria=None):
        try:
            mantenimientos = Mantenimientos.objects.filter(enable=1)
            serializer = self.get_serializer(mantenimientos, many=True)
            return Response(serializer.data)
        except Exception as e:
             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=False, methods=['delete'], url_path='logical/delete/(?P<id>[^/.]+)')
    def logical_delete(self,request, id=None):
        try:
            mantenimiento = Mantenimientos.objects.get(id=id)
            mantenimiento.enable = 0
            mantenimiento.save()
            return Response({'delete': 1})
        except Mantenimientos.DoesNotExist:
            return Response({'error': 'Mantenimiento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:  
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
