from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.v0.users.serializer import CreateSerializer, GetUserSerializer
from services.users.services import UserService
from users.models import User


class UserListView(APIView):
    def post(self, request):
        serializer = CreateSerializer(data=request.data)
        created_user = UserService().create(serializer)
        return Response(
            status=status.HTTP_201_CREATED,
            data=created_user.data,
        )

    def get(self, request):
        users = User.objects.all()
        serializer = GetUserSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
