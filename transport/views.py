from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Airplane, AirplaneType
from .serializers import AirplaneListSerializer, AirplaneDetailSerializer, AirplaneTypeSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    permission_classes = [IsAuthenticated,]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AirplaneDetailSerializer
        return AirplaneListSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
