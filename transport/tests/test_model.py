import pytest
from transport.models import Airplane, AirplaneType
from django.core.exceptions import ValidationError


"""Airplane model"""
@pytest.mark.django_db
def test_airplane_str_and_number_of_seats():
    airplane_type = AirplaneType.objects.create(name="test_plane")
    airplane = Airplane.objects.create(
        name="Test",
        rows=20,
        seats_in_row=6, 
        airplane_type=airplane_type
    )

    assert str(airplane) == "Test (120 seats)"


@pytest.mark.django_db
def test_airplane_invalid_rows_raises_error():
    airplane_type = AirplaneType.objects.create(name="test_plane")
    airplane = Airplane.objects.create(
        name="Test",
        rows=0,
        seats_in_row=6, 
        airplane_type=airplane_type
    )
    with pytest.raises(ValidationError):
        airplane.full_clean()


@pytest.mark.django_db
def test_airplane_invalid_seats_in_row_raises_error():
    airplane_type = AirplaneType.objects.create(name="test_plane")
    airplane = Airplane.objects.create(
        name="Test",
        rows=20,
        seats_in_row=0, 
        airplane_type=airplane_type
    )
    with pytest.raises(ValidationError):
        airplane.full_clean()


"""Airplane_type model"""
@pytest.mark.django_db
def test_airplane_type_str():
    airplane_type = AirplaneType.objects.create(name="test_plane")

    assert str(airplane_type) == "test_plane"
