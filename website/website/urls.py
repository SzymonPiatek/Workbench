from django.contrib import admin
from django.urls import path, include
from tastypie.api import Api
from . import views
from api.models import NotificationResource, CustomUserResource


api = Api(api_name='v1')

notification_resource = NotificationResource()
user_resource = CustomUserResource()

api.register(notification_resource)
api.register(user_resource)

urlpatterns = [
    path('', views.main_panel, name="main_panel_page"),
    path('admin/', admin.site.urls),
    path('statistics/', views.statistics, name="statistics_page"),
    path('notifications/', include("notifications.urls")),
    path('users/', include("users.urls")),

    path('api/', include(api.urls))
]
