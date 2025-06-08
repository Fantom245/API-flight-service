from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from .serializers import CrewSerializer, EmailAuthTokenSerializer


class CreateCrewViewSet(generics.CreateAPIView):
    serializer_class = CrewSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = EmailAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
