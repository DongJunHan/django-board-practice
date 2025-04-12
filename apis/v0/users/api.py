from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apis.v0.users.serializers import CreateSerializer, GetUserSerializer
from services.users.services import UserService
from users.models import User


class UserListViewSet(GenericAPIView):

    @action(methods=["GET", "POST"], detail=False, url_path="")
    def user_list(self, request):
        if request.method == "POST":
            serializer = CreateSerializer(data=request.data)
            created_user = UserService().create(serializer)
            return Response(
                status=status.HTTP_201_CREATED,
                data=created_user.data,
            )
        elif request.method == "GET":
            users = User.objects.all()
            serializer = GetUserSerializer(users, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)


class UserDetailViewSet(GenericAPIView):
    @action(methods=["GET"], detail=False, url_path="")
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        serializer = GetUserSerializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
