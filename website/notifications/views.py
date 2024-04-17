from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import Notification
from users.models import CustomUser
import json
from datetime import datetime


def format_datetime_data(date_str):
    try:
        date = date_str.replace("T", " ")
        date = datetime.strptime(date, '%Y-%m-%d %H:%M')
        return date
    except Exception as e:
        print(f"Error: {e}")


def format_datetime_data_to_str(date_str):
    try:
        date = str(date_str)[:16]
        return date
    except Exception as e:
        print(f"Error: {e}")


def get_notification_info(request, notification_id):
    if request.method == 'GET':
        try:
            notification = Notification.objects.get(pk=notification_id)
            recipients_emails = [user.email for user in notification.recipients.all()]
            data = {
                'title': notification.title,
                'message': notification.message,
                'created_at': format_datetime_data_to_str(date_str=notification.created_at),
                'notification_type': notification.type_name(),
                'recipientsList': recipients_emails,
                'isActive': notification.is_active_return(),
            }
            if notification.notification_type == 'single_use':
                data['date'] = notification.date
            elif notification.notification_type == 'cyclical':
                data['startDate'] = notification.start_date
                data['frequency'] = notification.frequency
            elif notification.notification_type == 'reminder':
                data['timeBefore'] = notification.time_before
            return JsonResponse(data, status=200)
        except Notification.DoesNotExist:
            return JsonResponse({'error': "Powiadomienie nie istnieje"}, status=404)
    else:
        return JsonResponse({'error': "Metoda HTTP nieobsługiwana"}, status=405)


@csrf_exempt
def save_notification(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            recipients_list_data = data['recipients']
            recipients_list = []
            for recipient in recipients_list_data:
                try:
                    user = CustomUser.objects.get(email=recipient)
                    recipients_list.append(user)
                except ObjectDoesNotExist:
                    pass

            new_notification = Notification.objects.create(
                title=data['title'],
                message=data['message'],
                notification_type=data['type'],
                is_active=data['isActive'] if data['isActive'] else False,
            )

            if data['type'] == "single_use":
                try:
                    new_notification.date = format_datetime_data(data['date'])
                except Exception as e:
                    print(f"Error: {e}")

            elif data['type'] == "cyclical":
                try:
                    new_notification.start_date = format_datetime_data(data['startDate'])
                except Exception as e:
                    print(f"Error: {e}")
                new_notification.frequency = data['frequency']
            elif data['type'] == "reminder":
                new_notification.time_before = data['timeBefore']

            new_notification.recipients.set(recipients_list)
            new_notification.save()
            return JsonResponse({'success': True})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'success': False, 'error': str(e)})

    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})


def notifications(request):
    all_notifications = Notification.objects.all()

    context = {
        "page_title": "Powiadomienia",
        "notifications": all_notifications,
    }

    return render(request, 'pages/notifications/notifications.html', context)
