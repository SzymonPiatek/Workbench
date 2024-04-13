from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_panel, name="main_panel_page"),
    path('statistics/', views.statistics, name="statistics_page"),
    path('notifications/', views.notifications, name="notifications_page"),
]
