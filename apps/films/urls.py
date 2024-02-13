from django.urls import path

from apps.films.views import get_Movies

urlpatterns = [
    path("films/", get_Movies),
]
