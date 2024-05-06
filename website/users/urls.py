from django.urls import path
from . import views


urlpatterns = [
    path('', views.users_list, name="users_page"),
    path('get_all_users/', views.get_all_users, name="get_all_users"),
]
