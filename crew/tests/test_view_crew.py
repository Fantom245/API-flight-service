import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_register_creates_user(api_client):
    """Проверка, что регистрация создаёт пользователя"""
    url = reverse("crew:create")
    data = {
        "email": "user@test.com",
        "password": "test123",
        "first_name": "John",
        "last_name": "Doe"
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED, response.data
    user = User.objects.get(email="user@test.com")
    assert user is not None
    assert user.check_password("test123")


@pytest.mark.django_db
def test_login_returns_token(api_client):
    """Проверка, что при логине возвращается токен"""
    user = User.objects.create_user(
        email="user@test.com",
        password="test123",
        first_name="John",
        last_name="Doe"
    )

    url = reverse("crew:get_token")
    data = {
        "email": "user@test.com",
        "password": "test123"
    }

    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_200_OK, response.data
    assert "token" in response.data
