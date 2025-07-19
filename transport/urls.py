from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AirplaneViewSet,
    AirplaneTypeViewSet
)

router = DefaultRouter()
router.register("airplane", AirplaneViewSet, basename="airplane")
router.register("airplane-type", AirplaneTypeViewSet, basename="airplane-type")

urlpatterns = [
    path("", include(router.urls)),
]   

app_name = "transport"
