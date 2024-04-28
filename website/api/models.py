from tastypie.resources import ModelResource
from notifications.models import Notification


class NotificationResource(ModelResource):
    class Meta:
        queryset = Notification.objects.all()
        resource_name = 'notifications'
        allowed_methods = ['get']
