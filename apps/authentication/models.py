from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField("Name", max_length=255, default=0)
    surname = models.CharField("Surname", max_length=255, null=True)
    birth_date = models.DateField("Birthday", null=True)
