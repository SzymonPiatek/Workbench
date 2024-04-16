from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'notification_type',
        'created_at',
        'count_recipients',
        'is_active',
    )
