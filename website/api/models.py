from tastypie.resources import ModelResource
from notifications.models import Notification
from users.models import CustomUser


class NotificationResource(ModelResource):
    class Meta:
        queryset = Notification.objects.all()
        resource_name = 'notifications'
        allowed_methods = ['get']


class CustomUserResource(ModelResource):
    class Meta:
        queryset = CustomUser.objects.all()
        resource_name = 'users'
        allowed_methods = ['get']
