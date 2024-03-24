from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.films.models import Movie
from apps.films.serializers import MovieSerializer


@api_view(["GET", "POST"])
@permission_classes([])
def movies_action(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        return Response({"films": MovieSerializer(movies, many=True).data})

    # POST
    serializer = MovieSerializer(data={
        "title": request.data.get("title"),
        "company": request.data.get("company"),
    })
    if serializer.is_valid():
        obj = serializer.save()
        return Response(MovieSerializer(obj).data, status=201)
    return Response({"errors": serializer.errors}, status=400)


@api_view(["PUT", "DELETE"])
@permission_classes([])
def movie_action(request, id: int):
    if request.method == "PUT":
        serializer = MovieSerializer(data={
            "title": request.data.get("title"),
            "company": request.data.get("company"),
        })
        if serializer.is_valid():
            Movie.objects.filter(id=id).update(**serializer.validated_data)
            return Response(status=200)
        return Response({"errors": serializer.errors}, status=400)

    # DELETE
    Movie.objects.filter(id=id).delete()
    return Response(status=204)
