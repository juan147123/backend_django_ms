from .api import SapMaestroRutBiViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('dwhperu', SapMaestroRutBiViewSet,'dwhperu')

urlpatterns = router.urls
