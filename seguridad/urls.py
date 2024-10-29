from rest_framework.routers import DefaultRouter

from seguridad.authapi import AplicacionUsuarioAuthViewSet
from .api import AplicacionUsuarioViewSet, RolAplicacionViewSet, UsuarioRolViewSet

router = DefaultRouter()
router.register('aplicacion-usuarios', AplicacionUsuarioViewSet, basename='aplicacionusuario')
router.register('roles-aplicacion', RolAplicacionViewSet, basename='rolaplicacion')
router.register('usuarios-rol', UsuarioRolViewSet, basename='usuariorol')
router.register('autenticacion', AplicacionUsuarioAuthViewSet, basename='autenticacion')


urlpatterns = router.urls
