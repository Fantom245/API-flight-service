from rest_framework import viewsets

from .models import Airplane, AirplaneType
from .serializers import AirplaneListSerializer, AirplaneDetailSerializer, AirplaneTypeSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AirplaneDetailSerializer
        return super().get_serializer_class()


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
