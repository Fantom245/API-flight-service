from rest_framework import viewsets

from .models import Airplane, AirplaneType
from .serializers import AirplaneListSerializer, AirplaneDetailSerializer, AirplaneTypeListSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AirplaneDetailSerializer
        return AirplaneListSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeListSerializer
