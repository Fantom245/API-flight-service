from rest_framework import generics

from .serializers import CrewSerializer


class CreateCrewViewSet(generics.CreateAPIView):
    serializer_class = CrewSerializer
