from django.urls import path

from apps.films.views import get_movies, create_movie, edit_movie, delete_movie

urlpatterns = [
    path("films/", get_movies,),
    path("create/", create_movie),
    path("edit/", edit_movie),
    path("delete/", delete_movie),
]
