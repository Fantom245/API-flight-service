from rest_framework import serializers

from .models import AirplaneType, Airplane


class AirplaneTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ["id", "name", "manufacturer", "max_range_km", "max_speed_kmh"]


class AirplaneListSerializer(serializers.ModelSerializer):
    number_of_seats = serializers.ReadOnlyField()
    
    class Meta:
        model = Airplane
        fields = ["id", "name", "rows", "seats_in_row", "number_of_seats", "airplane_type", "status"]


class AirplaneDetailSerializer(AirplaneListSerializer):
    airplane_type = serializers.SlugRelatedField(
        slug_field = "name",
        queryset = AirplaneType.objects.all()
    )
