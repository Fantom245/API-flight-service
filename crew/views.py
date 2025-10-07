from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model

from .serializers import CrewSerializer, EmailAuthTokenSerializer


class CreateCrewViewSet(generics.CreateAPIView):
    serializer_class = CrewSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny,]


class LoginCrewView(ObtainAuthToken):
    serializer_class = EmailAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageCrewView(generics.RetrieveUpdateAPIView):
    serializer_class = CrewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
