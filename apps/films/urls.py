from django.urls import path

from apps.films.views import get_movies, create_movie, edit_movie, delete_movie

urlpatterns = [
    path("films/", get_movies,),
    path("films/", create_movie),
    path("films/", edit_movie),
    path("films/", delete_movie),
]
