from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Crew
from .forms import CrewCreationForm


@admin.register(Crew)
class CrewAdmin(UserAdmin):
    add_form = CrewCreationForm
    model = Crew

    list_display = ("id", "username", "email", "first_name", "last_name", "birthday", "phone", "date_joined", "is_staff", "password")
    list_display_links = ("id", "username", "email")
    list_filter = ("is_staff", "date_joined")
    search_fields = ("username", "first_name", "last_name")
    readonly_fields = ("id", "date_joined",)
    ordering = ("-date_joined",)
    date_hierarchy = "date_joined"
    empty_value_display = "None"

    fieldsets = (
        (None, {
            "fields": ("email", "password")
        }),
        ("Personal information", {
            "fields": ("username", "first_name", "last_name", "birthday", "phone"),
        }),
        ("Flags", {
            "fields": ("is_staff", "is_active", "groups", "user_permissions")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "username",
                "phone",
                "birthday",
                "password1",
                "password2",
                "is_staff",
                "is_active",
                "groups",
                "user_permissions"
            ),
        }),
    )
