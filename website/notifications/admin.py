from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'message',
        'created_at',
        'start_date',
        'frequency',
        'count_recipients',
        'is_active',
    )
