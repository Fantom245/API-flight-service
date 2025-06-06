from django.shortcuts import render
from rest_framework import viewsets

from .models import Crew
from .serializers import CrewRegisterSerializer


class CrewRegisterViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewRegisterSerializer
