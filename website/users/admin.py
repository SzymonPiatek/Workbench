from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "full_name",
        "username",
        "room",
    )
    search_fields = (
        "full_name",
        "email",
        "room",
    )
