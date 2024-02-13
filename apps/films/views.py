from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.films.models import Movie
from apps.films.serializers import MovieSerializer


@api_view(["GET"])
@permission_classes([])
def get_movies(request):
    movies = Movie.objects.all()
    return Response({"films": MovieSerializer(movies, many=True).data})
