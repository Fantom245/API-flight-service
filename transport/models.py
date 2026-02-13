from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class AirplaneType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    max_range_km = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)]
    )
    max_speed_kmh = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        help_text=_("Maximum cruise speed in kilometers per hour (km/h).")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "name"]
        verbose_name = _("Airplane Type")
        verbose_name_plural = _("Airplane Types")

    def __str__(self):
        return self.name


class Airplane(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", _("Active")
        MAINTENANCE = "maintenance", _("Maintenance")
        RETIRED = "retired", _("Retired")

    name = models.CharField(max_length=255, unique=True)
    rows = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    seats_in_row = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def number_of_seats(self):
        return self.seats_in_row * self.rows
    
    class Meta:
        indexes = [
            models.Index(fields=["airplane_type"]),
        ]
        ordering = ["name",]
        verbose_name = _("Airplane")
        verbose_name_plural = _("Airplanes")

    def __str__(self):
        return f"{self.name} ({self.number_of_seats} seats)"
