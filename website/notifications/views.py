from django.shortcuts import render
from .models import Notification
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def save_notification(request):
    if request.method == 'POST':
        try:
            # Odczytujemy przesłane dane JSON
            data = json.loads(request.body.decode('utf-8'))

            # Tworzymy nowe powiadomienie na podstawie przesłanych danych
            new_notification = Notification.objects.create(
                title=data.get('title'),
                message=data.get('message'),
                notification_type=data.get('type'),
                date=data.get('date'),
                startDate=data.get('startDate'),
                frequency=data.get('frequency'),
                timeBefore=data.get('timeBefore'),
                recipients=data.get('recipients'),
                status=data.get('status')
            )
            new_notification.save()
            # Zwracamy potwierdzenie sukcesu w formie JSON
            return JsonResponse({'success': True})

        except Exception as e:
            # W razie błędu zwracamy informację o niepowodzeniu
            return JsonResponse({'success': False, 'error': str(e)})

    else:
        # Zwracamy błąd, jeśli żądanie nie jest typu POST
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})

def notifications(request):
    all_notifications = Notification.objects.all()

    context = {
        "page_title": "Powiadomienia",
        "notifications": all_notifications,
    }

    return render(request, 'pages/notifications/notifications.html', context)
