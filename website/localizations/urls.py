from django.urls import path
from . import views


urlpatterns = [
    path('', views.localizations_view, name="localizations_page"),
]
