from .api import MantenimientosViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('mantenimientos', MantenimientosViewSet,'mantenimientos')

urlpatterns = router.urls
