from .api import EvaluacionViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('evaluacion', EvaluacionViewSet,'evaluacion')

urlpatterns = router.urls
