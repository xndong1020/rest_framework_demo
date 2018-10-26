from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

    # override is_valid method
    def is_valid(self, raise_exception=False):
        print(self._kwargs["data"])
        valid = super(UserSerializer, self).is_valid(raise_exception=raise_exception)
        return valid

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
