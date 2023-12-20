from rest_framework import serializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}
