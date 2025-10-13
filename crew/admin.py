from django.contrib import admin
from .models import Crew


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "email", "date_joined", "is_staff")
    list_display_links = ("id", "username", "email")
    list_filter = ("is_staff", "date_joined")
    search_fields = ("username", "first_name", "last_name")
    readonly_fields = ("id", "date_joined",)
    ordering = ("-date_joined",)
    date_hierarchy = "date_joined"
    empty_value_display = "None"

    fieldsets = (
        (None, {
            "fields": ("username", "email") # разобраться с тем как хэшировать пароль и вводить его
        }),
        ("Personal information", {
            "fields": ("first_name", "last_name"),
        }),
        ("Flags", {
            "fields": ("is_staff", "is_active")
        }),
    )
