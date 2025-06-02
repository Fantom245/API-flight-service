from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class AirplaneType(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        error_messages={
            "unique": _("An airplane type with that name already exists."),
        },
    )

    class Meta:
        ordering = ["name",]
        verbose_name = _("Airplane Type")
        verbose_name_plural = _("Airplane Types")

    def __str__(self):
        return self.name


class Airplane(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True, 
        error_messages={
            "unique": _("An airplane with that name already exists."),
        },
    )
    rows = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    seats_in_row = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE)

    @property
    def number_of_seats(self):
        return self.seats_in_row * self.rows
    
    class Meta:
        ordering = ["name",]
        verbose_name = _("Airplane")
        verbose_name_plural = _("Airplanes")

    def __str__(self):
        return f"{self.name} ({self.number_of_seats} seats)"
