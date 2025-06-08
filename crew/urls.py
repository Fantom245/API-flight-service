from django.urls import path

from .views import CreateCrewViewSet, CreateTokenView


urlpatterns = [
    path("register/", CreateCrewViewSet.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token")
]

app_name = "crew"