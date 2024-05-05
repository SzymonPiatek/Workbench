from django.urls import path
from . import views


urlpatterns = [
    path('', views.localizations_view, name="localizations_page"),
    path('/localization/<int:localization_id>', views.localizations_rooms_view, name="localizations_rooms_page"),
    path('/localization/save', views.localization_save_view, name="save_localization_page"),
    path('/room/save', views.room_save_view, name="save_room_page"),
    path('/room/<int:room_id>', views.room_view, name="room_page"),
    path('/addresses', views.addresses, name="get_all_addresses"),
]
