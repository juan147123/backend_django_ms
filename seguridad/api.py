from rest_framework import viewsets, permissions, status, filters
from .models import AplicacionUsuario, RolAplicacion, UsuarioRol
from .serializer import AplicacionUsuarioSerializer, RolAplicacionSerializer, UsuarioRolSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class AplicacionUsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AplicacionUsuarioSerializer
    queryset = AplicacionUsuario.objects.using('seguridadapp').all()
    filterset_fields = ['id_aplicacion']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    @action(detail=False, methods=['post'], url_path='create_post')
    def create_post(self, request):

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

        aplicacion_usuario = AplicacionUsuario.objects.using(
            'seguridadapp').create(**serializer.validated_data)
        rol_data = {
            "id_rol": request.data.get("id_rol"),
            "pais": request.data.get("pais"),
            "objeto_permitido":request.data.get("id_ceco"),
            "id_aplicacion_usuario":aplicacion_usuario.id_aplicacion_usuario
        }
        usuario_rol = UsuarioRol.objects.create(**rol_data)

        return Response({
            "usuario": AplicacionUsuarioSerializer(aplicacion_usuario).data,
            "usuario_rol": UsuarioRolSerializer(usuario_rol).data
        }, status=status.HTTP_201_CREATED)


class RolAplicacionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RolAplicacionSerializer

    def get_queryset(self):
        return RolAplicacion.objects.using('seguridadapp').all()


class UsuarioRolViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioRolSerializer

    def get_queryset(self):
        return UsuarioRol.objects.using('seguridadapp').all()
