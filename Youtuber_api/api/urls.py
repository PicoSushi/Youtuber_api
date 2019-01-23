from rest_framework import routers
from .views import VtuberViewSet

router = routers.DefaultRouter()
router.register('vtuber', VtuberViewSet)
