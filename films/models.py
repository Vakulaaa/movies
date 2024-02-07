from django.db import models


class Movie:
    title = models.CharField("title", null=True)
