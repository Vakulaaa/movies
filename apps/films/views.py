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
def create_movie(request, title, company):
    if request.method == "POST":
        movie = Movie()
        movie.title = request.POST.get("title")
        movie.company = request.POST.get("company")
        if movie.is_valid():
            movie.save()
        else:
            return Response("invalid creating")
    return Response({"movie"})


# Updating
def edit_movie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST" and movie.is_valid():
        movie = Movie()
        movie.title = request.POST.get("title")
        movie.company = request.POST.get("company")
        movie.save()
    else:
        return Response("invalid editing")
    return Response({"movie"})


# Deleting
def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return Response("object deleted")
