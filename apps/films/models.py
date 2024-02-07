from django.db import models


class Movie(models.Model):
    title = models.CharField("Title", max_length=255)
