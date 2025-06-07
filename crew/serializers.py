from rest_framework import serializers

from .models import Crew


class CrewRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ["id", "first_name", "last_name", "email", "password"]

