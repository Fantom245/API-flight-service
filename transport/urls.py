from django.urls import path

from .views import AirplaneViewSet, AirplaneTypeViewSet


urlpatterns = [
    path("airplane/", AirplaneViewSet.as_view({"get": "list", "post": "create"}), name="airplane-list"),
    path("airplane-type/", AirplaneTypeViewSet.as_view({"get": "list", "post": "create"}), name="airplane-type-list")
]   

app_name = "transport"
