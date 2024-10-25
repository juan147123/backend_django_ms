from rest_framework.routers import DefaultRouter
from .api import RiesgosOportunidadesViewSet

router = DefaultRouter()
router.register('riesgos-oportunidades', RiesgosOportunidadesViewSet, basename='riesgosoportunidades')
urlpatterns = router.urls
