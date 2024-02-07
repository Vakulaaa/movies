from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField("Birthday", null=True)

class Movie:
    movie_name = models.CharField("title", null=True)
