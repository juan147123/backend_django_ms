from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from .models import SapMaestroRutBi, VwCecoConsolidadoGF
from .serializer import SapMaestroRutBiSerializer, CecosGFSerializer, UnidadesGFSerializer
from rest_framework.decorators import action


class SapMaestroRutBiViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SapMaestroRutBiSerializer

    def get_queryset(self):
        return SapMaestroRutBi.objects.using('dw_peru').all()

    @action(detail=False, methods=['get'], url_path='empresas')
    def activos(self, request):
        try:
            sap_maestro_rut_bi = SapMaestroRutBi.objects.using(
                'dw_peru').filter(base_vigente="Y")
            serializer = self.get_serializer(sap_maestro_rut_bi, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='unidades/(?P<ruc_empresa>[^/.]+)')
    def unidades(self, request, ruc_empresa=None):
        try:
            unidades = VwCecoConsolidadoGF.objects.using('dw_peru').filter(
                base_vigente_empresa="Y", ruc_empresa=ruc_empresa
            ).values('id_unidad_negocio', 'unidad_negocio_desc').distinct()
            serializer = UnidadesGFSerializer(unidades, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='centros/(?P<id_unidad_negocio>[^/.]+)/(?P<ruc_empresa>[^/.]+)')
    def centros(self, request, id_unidad_negocio=None, ruc_empresa=None):
        try:
            unidades = VwCecoConsolidadoGF.objects.using('dw_peru').filter(
                base_vigente_empresa="Y", id_unidad_negocio=id_unidad_negocio, ruc_empresa=ruc_empresa
            ).values('codigo_centro_gestion', 'centro_gestion_desc').distinct()
            serializer = CecosGFSerializer(unidades, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

