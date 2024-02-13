from rest_framework import serializers

from apps.films.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "Title",
            "year",
        ]
