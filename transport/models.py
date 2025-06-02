from django.db import models
from django.core.validators import MinValueValidator


class AirplaneType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name",]
        verbose_name = "Airplane Type"
        verbose_name_plural = "Airplane Types"

    def __str__(self):
        return self.name


class Airplane(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rows = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    seats_in_row = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE)

    @property
    def number_of_seats(self):
        return self.seats_in_row * self.rows
    
    class Meta:
        ordering = ["name",]
        verbose_name = "Airplane"
        verbose_name_plural = "Airplanes"

    def __str__(self):
        return f"{self.name} ({self.number_of_seats} seats)"
