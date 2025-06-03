from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from crew.models import Crew
from transport.models import Airplane


class Airport(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        error_messages={
            "unique": _("An airport with that name already exists.")
        }
    )
    closest_big_city = models.CharField(max_length=255)

    class Meta:
        ordering = ["name",]
        verbose_name = _("Airport")
        verbose_name_plural = _("Airports")

    def __str__(self):
        return self.name
    

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

    class Meta:
        verbose_name = _("Route")
        verbose_name_plural = _("Routes")

    def __str__(self):
        return f"{self.source} - {self.destination}"
    

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Crew, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at",]
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order by {self.user} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    

"""Работа с этим классом"""
class Ticket(models.Model):
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    flight = models.ForeignKey("Flight")
    order = models.ForeignKey(Order)

    def __str__(self):
        return self.row
    

class Flight(models.Model):
    route = models.ForeignKey(Route)
    airplane = models.ForeignKey(Airplane)
    departure_time = models.DateTimeField(auto_now_add=True)
    arrival_time = models.DateTimeField(auto_now_add=True)
