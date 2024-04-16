from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import Notification
from users.models import CustomUser
import json
from datetime import datetime


@csrf_exempt
def save_notification(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            recipients_list_data = data.get('recipients')
            recipients_list = []
            for recipient in recipients_list_data:
                try:
                    user = CustomUser.objects.get(email=recipient)
                    recipients_list.append(user)
                except ObjectDoesNotExist:
                    pass

            new_notification = Notification.objects.create(
                title=data.get('title'),
                message=data.get('message'),
                notification_type=data.get('type'),
                is_active=data.get('is_active') if data.get('is_active') else False,
            )

            if data['type'] == "single_use":
                date_str = data['date']
                date = date_str.replace("T", " ")
                try:
                    date = datetime.strptime(date, '%Y-%m-%d %H:%M')
                    new_notification.date = date
                    new_notification.save()
                except Exception as e:
                    print(e)

            elif data['type'] == "cyclical":
                print("cyclical")
            elif data['type'] == "reminder":
                print("reminder")

            # new_notification = Notification.objects.create(
            #     title=data.get('title'),
            #     message=data.get('message'),
            #     # date=data.get('date'),
            #     # startDate=data.get('startDate'),
            #     frequency=data.get('frequency'),
            #     timeBefore=data.get('timeBefore'),
            #     # status=data.get('status')
            # )
            # new_notification.recipients.set(recipients_list)
            # new_notification.save()
            #
            # print(new_notification)
            return JsonResponse({'success': True})

        except Exception as e:
            print("error")
            return JsonResponse({'success': False, 'error': str(e)})

    else:
        print("else")
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})

def notifications(request):
    all_notifications = Notification.objects.all()

    context = {
        "page_title": "Powiadomienia",
        "notifications": all_notifications,
    }

    return render(request, 'pages/notifications/notifications.html', context)
