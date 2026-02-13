import pytest
from flight_order.models import Route, Order, Ticket, Flight, Airport
from flight_order.serializers import (
    AirportSerializer,
    RouteSerializer,
    OrderSerializer,
    TicketSerializer,
    FlightSerializer
)
from crew.models import Crew
from transport.models import Airplane, AirplaneType
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


@pytest.mark.django_db
def test_airport_serializer():
    airport = Airport.objects.create(name="Test Airport", closest_big_city="CityX")
    serializer = AirportSerializer(airport)
    data = serializer.data
    assert data["name"] == "Test Airport"
    assert data["closest_big_city"] == "CityX"


@pytest.mark.django_db
def test_route_serializer():
    airport1 = Airport.objects.create(name="A1", closest_big_city="C1")
    airport2 = Airport.objects.create(name="A2", closest_big_city="C2")
    route = Route.objects.create(source=airport1, destination=airport2, distance=100)
    serializer = RouteSerializer(route)
    data = serializer.data
    assert data["source"] == airport1.id
    assert data["destination"] == airport2.id
    assert data["distance"] == 100

    route_same = Route(source=airport1, destination=airport1, distance=50)
    with pytest.raises(ValidationError):
        route_same.clean()


@pytest.mark.django_db
def test_order_serializer():
    user = Crew.objects.create_user(email="user@test.com", password="12345")
    order = Order.objects.create(user=user)
    serializer = OrderSerializer(order)
    data = serializer.data
    assert data["user"] == user.id


@pytest.mark.django_db
def test_flight_and_ticket_serializer():
    user = Crew.objects.create_user(email="user2@test.com", password="12345")
    airplane_type = AirplaneType.objects.create(name="Type1")
    airplane = Airplane.objects.create(name="Plane1", rows=10, seats_in_row=6, airplane_type=airplane_type)
    airport1 = Airport.objects.create(name="A3", closest_big_city="C3")
    airport2 = Airport.objects.create(name="A4", closest_big_city="C4")
    route = Route.objects.create(source=airport1, destination=airport2, distance=500)
    
    departure = datetime.now()
    arrival = departure + timedelta(hours=2)
    flight = Flight.objects.create(route=route, airplane=airplane, departure_time=departure, arrival_time=arrival)
    order = Order.objects.create(user=user)
    ticket = Ticket.objects.create(row=1, seat=1, flight=flight, order=order)

    flight_serializer = FlightSerializer(flight)
    ticket_serializer = TicketSerializer(ticket)

    assert flight_serializer.data["route"] == route.id
    assert flight_serializer.data["airplane"] == airplane.id
    assert ticket_serializer.data["flight"] == flight.id
    assert ticket_serializer.data["order"] == order.id
