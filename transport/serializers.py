from rest_framework import serializers

from .models import AirplaneType, Airplane


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ["id", "name"]


class AirplaneSerializer(serializers.ModelSerializer):
    airplane_type = serializers.SlugRelatedField(
        slug_field = "name",
        queryset = AirplaneType.objects.all()
    )
    
    class Meta:
        model = Airplane
        fields = ["id", "name", "rows", "seats_in_row", "airplane_type"]
