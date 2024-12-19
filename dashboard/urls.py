from .api import CentroGestionDashboardViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('dashboard', CentroGestionDashboardViewSet,'dashboard')

urlpatterns = router.urls
