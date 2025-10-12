from django.contrib import admin
from .models import Crew


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "full_name", "email", "date_joined", "is_staff")
    list_display_links = ("id", "username", "email")
    list_filter = ("is_staff", "date_joined")
    search_fields = ("username", "first_name", "last_name")
    readonly_fields = ("id", "date_joined",)
    ordering = ("-date_joined",)
    date_hierarchy = "date_joined"

    fieldsets = (
        (None, {
            "fields": ("username", "email")
        }),
        ("Personal information", {
            "fields": ("first_name", "last_name"),
            "classes": ("collapse",)
        }),
        ("Flags", {
            "fields": ("is_staff", "is_active")
        }),
    )
