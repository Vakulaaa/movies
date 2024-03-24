from django.urls import path

from apps.films.views import movie_action, movies_action

urlpatterns = [
    path("films/", movies_action, name='get-create-movie'),
    path("films/<int:id>/", movie_action, name='put-delete-movie'),
]
