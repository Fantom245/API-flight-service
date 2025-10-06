import pytest
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

from crew.models import Crew
from transport.models import Airplane, AirplaneType
from flight_order.models import Airport, Route, Flight, Order, Ticket


@pytest.mark.django_db
def test_airport_str():
    airport = Airport.objects.create(name="Kyiv", closest_big_city="Kyiv")
    assert str(airport) == "Kyiv"


@pytest.mark.django_db
def test_route_str_and_validation():
    airport1 = Airport.objects.create(name="Kyiv", closest_big_city="Kyiv")
    airport2 = Airport.objects.create(name="Lviv", closest_big_city="Lviv")

    route = Route.objects.create(source=airport1, destination=airport2, distance=500)
    assert str(route) == f"{airport1} - {airport2}"

    route_same = Route(source=airport1, destination=airport1, distance=100)
    with pytest.raises(ValidationError):
        route_same.clean()


@pytest.mark.django_db
def test_order_str():
    user = Crew.objects.create_user(email="test@test.com", password="12345")
    order = Order.objects.create(user=user)
    assert str(order).startswith(f"Order by {user}")


@pytest.mark.django_db
def test_ticket_unique_and_str():
    user = Crew.objects.create_user(email="test@test.com", password="12345")
    airport1 = Airport.objects.create(name="Kyiv", closest_big_city="Kyiv")
    airport2 = Airport.objects.create(name="Lviv", closest_big_city="Lviv")
    route = Route.objects.create(source=airport1, destination=airport2, distance=500)
    airplane_type = AirplaneType.objects.create(name="TestType")
    airplane = Airplane.objects.create(
        name="TestPlane",
        rows=10,
        seats_in_row=6,
        airplane_type=airplane_type
    )
    flight = Flight.objects.create(
        route=route,
        airplane=airplane,
        departure_time=datetime.now(),
        arrival_time=datetime.now() + timedelta(hours=2)
    )
    order = Order.objects.create(user=user)

    ticket = Ticket.objects.create(flight=flight, order=order, row=1, seat=1)
    assert str(ticket) == f"Ticket: Row 1, Seat 1, Flight {flight}"

    with pytest.raises(Exception):
        Ticket.objects.create(flight=flight, order=order, row=1, seat=1)


@pytest.mark.django_db
def test_flight_str():
    airport1 = Airport.objects.create(name="Kyiv", closest_big_city="Kyiv")
    airport2 = Airport.objects.create(name="Lviv", closest_big_city="Lviv")
    route = Route.objects.create(source=airport1, destination=airport2, distance=500)
    airplane_type = AirplaneType.objects.create(name="TestType")
    airplane = Airplane.objects.create(name="TestPlane", rows=10, seats_in_row=6, airplane_type=airplane_type)
    departure = datetime.now()
    arrival = departure + timedelta(hours=2)
    flight = Flight.objects.create(route=route, airplane=airplane, departure_time=departure, arrival_time=arrival)
    assert str(flight) == f"{route} at {departure.strftime('%Y-%m-%d %H:%M')}"
