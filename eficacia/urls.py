from .api import EficaciaViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('eficacia', EficaciaViewSet,'eficacia')

urlpatterns = router.urls
