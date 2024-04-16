from django.urls import path
from . import views


urlpatterns = [
    path('', views.notifications, name="notifications_page"),
    path('save/', views.save_notification, name="save_notification_page"),
]
