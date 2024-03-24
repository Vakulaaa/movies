from django.contrib import admin
from django.urls import path
from apps.authentication.urls import urlpatterns as user_urlpatterns
from apps.films.urls import urlpatterns as films_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    *user_urlpatterns,
    *films_urlpatterns
]
