from rest_framework import serializers

from users.models import User


class CreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=200, write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "name", "password")

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class GetUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "name"]
