from rest_framework import serializers

from .models import AirplaneType, Airplane


class AirplaneTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ["id", "name", "manufacturer", "max_range_km", "max_speed_kmh"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AirplaneListSerializer(serializers.ModelSerializer):
    number_of_seats = serializers.ReadOnlyField()
    airplane_type = serializers.SlugRelatedField(
        slug_field = "name",
        queryset = AirplaneType.objects.all()
    )

    class Meta:
        model = Airplane
        fields = ["id", "name", "rows", "seats_in_row", "number_of_seats", "airplane_type", "status"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AirplaneDetailSerializer(AirplaneListSerializer):
    airplane_type = serializers.SlugRelatedField(
        slug_field = "name",
        queryset = AirplaneType.objects.all()
    )
