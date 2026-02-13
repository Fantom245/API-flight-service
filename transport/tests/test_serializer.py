import pytest
from transport.models import Airplane, AirplaneType
from transport.serializers import AirplaneTypeSerializer, AirplaneListSerializer, AirplaneDetailSerializer


@pytest.mark.django_db
def test_airplane_type_serializer():
    airplane_type = AirplaneType.objects.create(name="Boeing")
    serializer = AirplaneTypeSerializer(airplane_type)

    assert serializer.data["id"] == airplane_type.id
    assert serializer.data["name"] == "Boeing"


@pytest.mark.django_db
def test_airplane_list_serializer():
    airplane_type = AirplaneType.objects.create(name="Boeing")
    airplane = Airplane.objects.create(
        name="Boeing 737",
        rows=20,
        seats_in_row=6,
        airplane_type=airplane_type
    )
    serializer = AirplaneListSerializer(airplane)

    data = serializer.data
    assert data["name"] == "Boeing 737"
    assert data["rows"] == 20
    assert data["seats_in_row"] == 6
    assert data["number_of_seats"] == 120
    assert data["airplane_type"] == airplane_type.id


@pytest.mark.django_db
def test_airplane_detail_serializer():
    airplane_type = AirplaneType.objects.create(name="Airbus")
    airplane = Airplane.objects.create(
        name="Airbus A320",
        rows=25,
        seats_in_row=6,
        airplane_type=airplane_type
    )
    serializer = AirplaneDetailSerializer(airplane)

    data = serializer.data
    assert data["airplane_type"] == "Airbus"
    assert data["number_of_seats"] == 150
    assert data["name"] == "Airbus A320"
