import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from crew.models import Crew
from flight_order.models import Airport, Route, Order, Ticket, Flight
from transport.models import Airplane


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return Crew.objects.create_user(email="test@test.com", password="12345")


@pytest.mark.django_db
def test_airport_list_requires_auth(api_client):
    url = reverse("flight_order:airport-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_airport_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("flight_order:airport-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_route_list_requires_auth(api_client):
    url = reverse("flight_order:route-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_route_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("flight_order:route-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_order_list_requires_auth(api_client):
    url = reverse("flight_order:order-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_order_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("flight_order:order-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_ticket_list_requires_auth(api_client):
    url = reverse("flight_order:ticket-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_ticket_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("flight_order:ticket-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_flight_list_requires_auth(api_client):
    url = reverse("flight_order:flight-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_flight_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("flight_order:flight-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
