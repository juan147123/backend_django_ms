from .api import RiesgosOportunidadesEncabezadoViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('encabezado', RiesgosOportunidadesEncabezadoViewSet,'encabezado')

urlpatterns = router.urls
