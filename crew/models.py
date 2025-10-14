from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
       extra_fields.setdefault("is_staff", True)
       extra_fields.setdefault("is_superuser", True)

       if extra_fields.get("is_staff") is not True:
           raise ValueError("Superuser must have is_staff=True.")
          
       if extra_fields.get("is_superuser") is not True:
           raise ValueError("Superuser must have is_superuser=True.")

       return self._create_user(email, password, **extra_fields)


class Crew(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return "Name not defined."

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["username", "email",]

    def __str__(self):
        return f"Username: {self.username}. Full_name: {self.full_name}. Email: {self.email}"
