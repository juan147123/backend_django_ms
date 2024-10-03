from .api import CentroGestionViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('centrogestion', CentroGestionViewSet,'centrogestion')

urlpatterns = router.urls
