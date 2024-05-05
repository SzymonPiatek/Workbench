from django.urls import path
from . import views


urlpatterns = [
    path('', views.localizations_view, name="localizations_page"),
    path('localization/<int:localization_id>', views.localizations_rooms_view, name="localizations_rooms_page"),
    path('/save', views.localization_save_view, name="save_localization_page")
]
