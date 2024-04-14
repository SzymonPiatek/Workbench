from django.contrib import admin
from django.urls import path, include
from . import views
from . import apis


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_panel, name="main_panel_page"),
    path('statistics/', views.statistics, name="statistics_page"),
    path('notifications/', include("notifications.urls")),

    path('get_all_users/', apis.get_all_users, name="get_all_users_api")
]
