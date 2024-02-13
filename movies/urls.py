from django.contrib import admin
from django.urls import path
from apps.authentication.urls import urlpatterns as user_urlpatterns

urlpatterns = [path("admin/", admin.site.urls), *user_urlpatterns]
