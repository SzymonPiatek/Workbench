from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from notifications.models import Notification
from users.models import CustomUser


class NotificationResource(ModelResource):
    class Meta:
        queryset = Notification.objects.all()
        resource_name = 'notifications'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()


class CustomUserResource(ModelResource):
    class Meta:
        queryset = CustomUser.objects.all()
        resource_name = 'users'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
