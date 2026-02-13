import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from crew.models import Crew

from transport.models import Airplane, AirplaneType


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return Crew.objects.create_user(email="test@test.com", password="12345")


@pytest.mark.django_db
def test_airplane_list_requires_auth(api_client):
    url = reverse("transport:airplane-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_airplane_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("transport:airplane-list")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_airplane_list_returns_objects(api_client, user):
    api_client.force_authenticate(user=user)
    
    airplane_type = AirplaneType.objects.create(name="Type A")
    airplane = Airplane.objects.create(
        name="Plane 1",
        rows=20,
        seats_in_row=6,
        airplane_type=airplane_type
    )
    
    url = reverse("transport:airplane-list")
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Plane 1"


@pytest.mark.django_db
def test_airplane_detail_view(api_client, user):
    api_client.force_authenticate(user=user)
    
    airplane_type = AirplaneType.objects.create(name="Type A")
    airplane = Airplane.objects.create(
        name="Plane 1",
        rows=20,
        seats_in_row=6,
        airplane_type=airplane_type
    )
    
    url = reverse("transport:airplane-detail", args=[airplane.id])
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert response.data["name"] == "Plane 1"
    assert response.data["number_of_seats"] == 120
    assert response.data["airplane_type"] == "Type A"


@pytest.mark.django_db
def test_airplane_create(api_client, user):
    api_client.force_authenticate(user=user)
    
    airplane_type = AirplaneType.objects.create(name="Type A")
    url = reverse("transport:airplane-list")
    
    data = {
        "name": "Plane 2",
        "rows": 10,
        "seats_in_row": 4,
        "airplane_type": airplane_type.id
    }
    
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert Airplane.objects.filter(name="Plane 2").exists()


@pytest.mark.django_db
def test_airplane_update(api_client, user):
    api_client.force_authenticate(user=user)
    
    airplane_type = AirplaneType.objects.create(name="Type A")
    airplane = Airplane.objects.create(
        name="Plane 3",
        rows=10,
        seats_in_row=4,
        airplane_type=airplane_type
    )
    
    url = reverse("transport:airplane-detail", args=[airplane.id])
    data = {"name": "Updated Plane"}
    
    response = api_client.patch(url, data)
    assert response.status_code == 200
    airplane.refresh_from_db()
    assert airplane.name == "Updated Plane"


@pytest.mark.django_db
def test_airplane_delete(api_client, user):
    api_client.force_authenticate(user=user)
    
    airplane_type = AirplaneType.objects.create(name="Type A")
    airplane = Airplane.objects.create(
        name="Plane 4",
        rows=10,
        seats_in_row=4,
        airplane_type=airplane_type
    )
    
    url = reverse("transport:airplane-detail", args=[airplane.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Airplane.objects.filter(id=airplane.id).exists()


@pytest.mark.django_db
def test_airplane_type_list_requires_auth(api_client):
    url = reverse("transport:airplane-type-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_airplane_type_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("transport:airplane-type-list")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_airplane_type_list_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    AirplaneType.objects.create(name="Type A")
    url = reverse("transport:airplane-type-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Type A"


@pytest.mark.django_db
def test_airplane_type_retrieve(api_client, user):
    api_client.force_authenticate(user=user)
    airplane_type = AirplaneType.objects.create(name="Type B")
    url = reverse("transport:airplane-type-detail", args=[airplane_type.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == "Type B"


@pytest.mark.django_db
def test_airplane_type_create(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("transport:airplane-type-list")
    data = {"name": "Type C"}
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert AirplaneType.objects.filter(name="Type C").exists()


@pytest.mark.django_db
def test_airplane_type_update(api_client, user):
    api_client.force_authenticate(user=user)
    airplane_type = AirplaneType.objects.create(name="Type D")
    url = reverse("transport:airplane-type-detail", args=[airplane_type.id])
    data = {"name": "Updated Type D"}
    response = api_client.patch(url, data)
    assert response.status_code == 200
    airplane_type.refresh_from_db()
    assert airplane_type.name == "Updated Type D"


@pytest.mark.django_db
def test_airplane_type_delete(api_client, user):
    api_client.force_authenticate(user=user)
    airplane_type = AirplaneType.objects.create(name="Type E")
    url = reverse("transport:airplane-type-detail", args=[airplane_type.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not AirplaneType.objects.filter(id=airplane_type.id).exists()
