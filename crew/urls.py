from django.urls import path

from .views import CrewRegisterViewSet


urlpatterns = [
    path("registration/", CrewRegisterViewSet.as_view({"post": "create"}), name="registration")
]

app_name = "crew"