from rest_framework.exceptions import ValidationError

from apis.v0.users.serializer import CreateSerializer
from users.models import User


class UserService:
    def create(self, user_data: CreateSerializer) -> CreateSerializer:
        if user_data.is_valid():
            user_data.save()
            return user_data

        raise ValidationError()
