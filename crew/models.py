from django.db import models
from django.contrib.auth.models import AbstractUser


class Crew(AbstractUser):
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return self.full_name
