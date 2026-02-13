from django.contrib import admin

from .models import Country, Airport, Route, Order, Ticket, Flight


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    list_display_links = ("id", "name", "code")
    list_per_page = 25
    search_fields = ("name",)
    ordering = ("name", "code")

    fieldsets = (
        ("Country", {
            "fields": ("name", "code")
        }),
    )


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "closest_big_city", "country")
    list_display_links = ("id", "name", "code")
    list_filter = ("country",)
    list_per_page = 25
    search_fields = ("name", "code", "country")
    ordering = ("name", "country")

    fieldsets = (
        (None, {
            "fields": ("name", "code", "closest_big_city", "country")
        }),
    )

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("id", "source", "destination", "distance", "estimated_duration")
    list_filter = ("distance", "estimated_duration")
    list_per_page = 25
    search_fields = ("distance",)
    
    fieldsets = (
        (None, {
            "fields": ("source", "destination", "distance")
        }),
        ("Time", {
            "fields": ("estimated_duration",)
        })
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_display_links = ("id", "user")
    list_filter = ("created_at",)
    list_per_page = 25
    search_fields = ("user",)
    readonly_fields = ("id", "created_at")
    ordering = ("-created_at",)

    fieldsets = (
        (None, {
            "fields": ("user", "created_at")
        }),
    )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "row", "seat", "flight", "order", "created_at", "updated_at")
    list_filter = ("flight", "created_at")
    list_per_page = 25
    search_fields = ("flight",)
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("-created_at",)

    fieldsets = (
        (None, {
            "fields": ("row", "seat", "flight", "order")
        }),
    )


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "route", "airplane", "crew", "departure_time", "arrival_time")
    list_filter = ("departure_time", "arrival_time")
    list_per_page = 25
    search_fields = ("aiplane", "crew")
    ordering = ("departure_time",)

    fieldsets = (
        (None, {
            "fields": ("route", "airplane", "crew")
        }),
        ("Time", {
            "fields": ("departure_time", "arrival_time")
        })
    )