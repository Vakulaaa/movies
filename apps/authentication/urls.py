from django.urls import path

from apps.authentication.views import get_users

urlpatterns = [
    path("users/", get_users),
]
