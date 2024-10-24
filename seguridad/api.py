import os
from rest_framework import viewsets, permissions, status, filters
from .models import AplicacionUsuario, RolAplicacion, UsuarioRol
from .serializer import AplicacionUsuarioSerializer, RolAplicacionSerializer, UsuarioRolSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


class AplicacionUsuarioFilter(django_filters.FilterSet):
    objeto_permitido = django_filters.CharFilter(
        field_name='usuariorol__objeto_permitido', lookup_expr='exact')

    class Meta:
        model = AplicacionUsuario
        fields = ['username', 'objeto_permitido']


class AplicacionUsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AplicacionUsuarioSerializer
    queryset = AplicacionUsuario.objects.using('seguridadapp').filter(
        id_aplicacion=os.getenv("ID_APLICACION"),
        usuariorol__estado=1
    ).prefetch_related('usuariorol_set')
    filterset_class = AplicacionUsuarioFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    def build_aplicacion_usuario(self, request):
        usuario_data = {
            "id_aplicacion": request.data.get("id_aplicacion"),
            "username": request.data.get("username"),
            "name": request.data.get("name"),
            "provider": request.data.get("provider"),
            "provider_id": request.data.get("provider_id"),
            "nombres": request.data.get("nombres"),
            "apellidos": request.data.get("apellidos"),
            "pais": request.data.get("pais"),
            "avatar": request.data.get("avatar"),
        }

        serializer = self.get_serializer(data=usuario_data)
        serializer.is_valid(raise_exception=True)
        return serializer

    def build_rol_usuario(self, request, aplicacion_usuario):
        rol_data = {
            "id_rol": request.data.get("id_rol"),
            "pais": request.data.get("pais"),
            "objeto_permitido": request.data.get("id_ceco"),
            "id_aplicacion_usuario": aplicacion_usuario,
        }
        return rol_data

    @action(detail=False, methods=['post'], url_path='create_post')
    def create_post(self, request):
        username = request.data.get("username")
        id_rol = request.data.get("id_rol")
        aplicacion_usuario = AplicacionUsuario.objects.using('seguridadapp').filter(
            username=username, id_aplicacion=os.getenv("ID_APLICACION")).first()

        if not aplicacion_usuario:
            serializer = self.build_aplicacion_usuario(request)
            aplicacion_usuario = AplicacionUsuario.objects.using(
                'seguridadapp').create(**serializer.validated_data)

        rol_aplicacion = RolAplicacion.objects.using(
            'seguridadapp').filter(id_rol=id_rol).first()

        if not rol_aplicacion:
            return Response({"error": "Rol no encontrado"}, status=status.HTTP_400_BAD_REQUEST)

        rol_data = self.build_rol_usuario(request, aplicacion_usuario)

        rol_data['id_rol'] = rol_aplicacion

        UsuarioRol.objects.using('seguridadapp').create(**rol_data)

        return Response(status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'], url_path='filtrar-por-objeto-permitido')
    def filtrar_por_objeto_permitido(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        filtered_data = []
        unique_users = set()  
        for data in serializer.data:
            if data['id_aplicacion_usuario'] not in unique_users:
                filtered_roles = [
                    rol for rol in data['usuariorol_set'] if rol['objeto_permitido'] == request.query_params.get("objeto_permitido")
                ]
                if filtered_roles:
                    data['usuariorol_set'] = filtered_roles
                    filtered_data.append(data)
                    unique_users.add(data['id_aplicacion_usuario']) 

        return Response(filtered_data, status=status.HTTP_200_OK)
class RolAplicacionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RolAplicacionSerializer

    def get_queryset(self):
        return RolAplicacion.objects.using('seguridadapp').filter(
            id_aplicacion=os.getenv("ID_APLICACION")
        )


class UsuarioRolViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioRolSerializer

    def get_queryset(self):
        return UsuarioRol.objects.using('seguridadapp').all()
