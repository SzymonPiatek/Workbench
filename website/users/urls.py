from django.urls import path
from . import apis


urlpatterns = [
    path('get_all_users/', apis.get_all_users, name="get_all_users_api")
]
