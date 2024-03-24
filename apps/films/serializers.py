from rest_framework import serializers

from apps.films.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "company"]
