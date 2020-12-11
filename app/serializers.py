# from django.contrib.auth.models import User as DjangoUser

from rest_framework import serializers

from .models import User, Task


# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # Password is write only!

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
