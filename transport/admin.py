from django.contrib import admin

from .models import Airplane, AirplaneType


@admin.register(AirplaneType)
class AirplaneTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "manufacturer", "max_range_km", "max_speed_kmh", "created_at", "updated_at")
    list_display_links = ("id", "name")
    list_filter = ("max_range_km", "created_at",) # сделать кастомный RangeFilter
    list_per_page = 25
    search_fields = ("name", "manufacturer")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("-created_at", "name",)
    date_hierarchy = "created_at"

    fieldsets = (
        (None, {
            "fields": ("name", "manufacturer")
        }),
        ("Characteristics", {
            "fields": ("max_range_km", "max_speed_kmh")
        })
    )


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rows", "seats_in_row", "number_of_seats", "airplane_type", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("created_at",)
    search_fields = ("name",)
    readonly_fields = ("id", "rows", "seats_in_row", "number_of_seats", "airplane_type", "created_at")
    ordering = ("name", "created_at")
    date_hierarchy = "created_at"

