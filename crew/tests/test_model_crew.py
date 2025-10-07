import pytest
from crew.models import Crew


@pytest.mark.django_db
def test_create_user_success():
    user = Crew.objects.create_user(email="user@test.com", password="pass123")
    assert user.email == "user@test.com"
    assert user.check_password("pass123")
    assert user.is_staff is False
    assert user.is_superuser is False


@pytest.mark.django_db
def test_create_superuser_success():
    admin = Crew.objects.create_superuser(email="admin@test.com", password="admin123")
    assert admin.email == "admin@test.com"
    assert admin.is_staff is True
    assert admin.is_superuser is True


@pytest.mark.django_db
def test_create_user_without_email_raises_error():
    with pytest.raises(ValueError):
        Crew.objects.create_user(email="", password="pass123")


@pytest.mark.django_db
def test_full_name_property():
    user = Crew.objects.create_user(email="user@test.com", password="pass123", first_name="John", last_name="Doe")
    assert user.full_name == "John Doe"


@pytest.mark.django_db
def test_str_returns_full_name():
    user = Crew.objects.create_user(email="user@test.com", password="pass123", first_name="John", last_name="Doe")
    assert str(user) == "John Doe"
