from django.shortcuts import render
from .models import Notification


def notifications(request):
    all_notifications = Notification.objects.all()

    context = {
        "page_title": "Powiadomienia",
        "notifications": all_notifications,
    }

    return render(request, 'pages/notifications.html', context)
