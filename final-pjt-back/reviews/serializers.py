from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from accounts.models import User
from .models import Review

user = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('nickname',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content', 'rate', 'user', 'id','movie')

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('title', 'content', 'rate', 'user')

class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title')

