from django.contrib.auth.models import User as DjangoUser

from rest_framework import serializers

from .models import User, Task


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # Password is write only!

    def create(self, validated_data):
        password = validated_data.pop('password')
        django_user = DjangoUser(**validated_data)
        django_user.set_password(password)
        django_user.save()
        return django_user
