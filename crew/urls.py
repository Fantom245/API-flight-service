from django.urls import path

from .views import CreateCrewViewSet


urlpatterns = [
    path("register/", CreateCrewViewSet.as_view(), name="create")
]

app_name = "crew"