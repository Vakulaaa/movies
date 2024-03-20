from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.films.models import Movie
from apps.films.serializers import MovieSerializer


@api_view(["GET"])
@permission_classes([])
def get_movies(request):
    movies = Movie.objects.all()
    return Response({"films": MovieSerializer(movies, many=True).data})


# Creating
@api_view(["POST"])
def create_movie(request, title, company):
    movie = Movie()
    movie.title = request.POST.get("title")
    movie.company = request.POST.get("company")
    if movie.is_valid():
        movie.save()
    else:
        return HttpResponse(status_code=403)
    return HttpResponse(status_code=200)


# Updating
@api_view(["PUT"])
def edit_movie(request, id):
    movie = Movie.objects.get(id=id)
    movie = Movie()
    movie.title = request.PUT.get("title")
    movie.company = request.PUT.get("company")
    movie.save()
    return HttpResponse(status_code=200)


# Deleting
@api_view(["DELETE"])
def delete_movie(request, id):
    Movie.objects.get(id=id).delete()
    return HttpResponse(status_code=204)
