from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from crew.models import Crew
from transport.models import Airplane


code_validator = RegexValidator(
    regex=r"[A-Z]{3,4}$",
    message=_("Code must be 3 or 4 uppercase Latin letters.")
)


class Country(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        error_messages={
            "unique": _("An airport with that name already exists.")
        }
    )
    code = models.CharField(
        max_length=4,
        unique=True,
        validators=[code_validator],
        help_text=_("Official IATA or ICAO airport code.")
    )
    closest_big_city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name",]
        verbose_name = _("Airport")
        verbose_name_plural = _("Airports")
        constraints = [
            models.UniqueConstraint(
                fields=["name", "country"],
                name="unique_airport_name_per_country"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"
    

class Route(models.Model):
    source = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="routes_from"
    )
    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="routes_to"
    )
    distance = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    estimated_duration = models.DurationField(null=True, blank=True)

    class Meta:
        verbose_name = _("Route")
        verbose_name_plural = _("Routes")
        constraints = [
            models.UniqueConstraint(
                fields=["source", "destination"],
                name="unique_route"
            )
        ]

    def clean(self):
        if self.source == self.destination:
            raise ValidationError(_("Source and destination cannot be the same."))

    def __str__(self):
        return f"{self.source} - {self.destination}"
    

class Order(models.Model):
    user = models.ForeignKey(Crew, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at",]
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order by {self.user} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    

class Ticket(models.Model):
    row = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    seat = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["flight", "row", "seat"]
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")
        constraints = [
            models.UniqueConstraint(
                fields=["flight", "row", "seat"],
                name="unique_flight_row_seat"
            )
        ]

    def __str__(self):
        return f"Ticket: Row {self.row}, Seat {self.seat}, Flight {self.flight}"


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.SET_NULL, null=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    class Meta:
        ordering = ["route", "airplane"]
        verbose_name = _("Flight")
        verbose_name_plural = _("Flights")

    def clean(self):
        if self.arrival_time <= self.departure_time:
            raise ValidationError(_("Arrival time must be after departure time."))

    def __str__(self):
        return f"{self.route} at {self.departure_time.strftime('%Y-%m-%d %H:%M')}"
