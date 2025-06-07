from rest_framework import serializers

from .models import AirplaneType, Airplane


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ["id", "name"]


class AirplaneListSerializer(serializers.ModelSerializer):
    number_of_seats = serializers.ReadOnlyField()
    
    class Meta:
        model = Airplane
        fields = ["id", "name", "rows", "seats_in_row", "number_of_seats", "airplane_type"]


class AirplaneDetailSerializer(AirplaneListSerializer):
    airplane_type = serializers.SlugRelatedField(
        slug_field = "name",
        queryset = AirplaneType.objects.all()
    )
