from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer


@api_view(["GET"])
@permission_classes([])
def get_users(request):
    users = User.objects.filter(is_active=True).all()
    return Response({"users": UserSerializer(users, many=True).data})
