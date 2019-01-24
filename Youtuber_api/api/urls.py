from rest_framework import routers
from .views import VtuberViewSet, YoutuberViewSet

router = routers.DefaultRouter()
router.register('vtuber', VtuberViewSet)
router.register('youtuber', YoutuberViewSet)
