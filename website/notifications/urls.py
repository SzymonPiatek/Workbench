from django.urls import path
from . import views


urlpatterns = [
    path('', views.notifications, name="notifications_page"),
    path('save/', views.save_notification, name="save_notification_page"),
    path('<int:notification_id>/info', views.get_notification_info, name='get_notification_info_page'),
    path('<int:notification_id>/delete', views.delete_notification, name='delete_notification_page'),
]
