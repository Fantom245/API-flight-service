from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AirportViewSet,
    RouteViewSet,
    OrderViewSet,
    TicketViewSet,
    FlightViewSet,
)

router = DefaultRouter()
router.register("airport", AirportViewSet, basename="airport")
router.register("route", RouteViewSet, basename="route")
router.register("order", OrderViewSet, basename="order")
router.register("ticket", TicketViewSet, basename="ticket")
router.register("flight", FlightViewSet, basename="flight")

urlpatterns = [
    path("", include(router.urls)),
]   

app_name = "flight_order"