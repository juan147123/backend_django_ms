from .api import ControlesViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('controles', ControlesViewSet,'controles')

urlpatterns = router.urls
