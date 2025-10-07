import pytest
from rest_framework.exceptions import ValidationError
from crew.serializers import EmailAuthTokenSerializer
from crew.models import Crew
from crew.serializers import CrewSerializer


@pytest.mark.django_db
def test_crew_serializer_creates_user():
    data = {"email": "user@test.com", "password": "test123"}
    serializer = CrewSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert Crew.objects.filter(email="user@test.com").exists()
    assert user.check_password("test123")


@pytest.mark.django_db
def test_email_auth_token_serializer_valid_credentials():
    Crew.objects.create_user(email="user@test.com", password="test123")
    data = {"email": "user@test.com", "password": "test123"}
    serializer = EmailAuthTokenSerializer(data=data)
    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_email_auth_token_serializer_invalid_password():
    Crew.objects.create_user(email="user@test.com", password="test123")
    data = {"email": "user@test.com", "password": "wrongpass"}
    serializer = EmailAuthTokenSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_email_auth_token_serializer_nonexistent_user():
    data = {"email": "no_user@test.com", "password": "test123"}
    serializer = EmailAuthTokenSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
