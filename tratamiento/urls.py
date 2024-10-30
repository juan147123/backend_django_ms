from .api import TratamientoViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('tratamiento', TratamientoViewSet,'tratamiento')

urlpatterns = router.urls
