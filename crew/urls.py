from django.urls import path
from rest_framework.authtoken import views

from .views import CreateCrewViewSet, LoginCrewView, ManageCrewView


urlpatterns = [
    path("register/", CreateCrewViewSet.as_view(), name="create"),
    path("login/", LoginCrewView.as_view(), name="get_token"),
    path("me/", ManageCrewView.as_view(), name="manage_user"),
]

app_name = "crew"
