from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=get_user_model()
        fields=('username','password','nickname','genre_preference','id')

class UserFollowSerializer(serializers.ModelSerializer):

    class Meta:
        model=get_user_model()
        fields=('username', 'followings')

class getUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=get_user_model()
        fields=('username','nickname',)