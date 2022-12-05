from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TicketList, Comment
from accounts.models import User

user = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class TicketListListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketList
        fields=('title', 'content', 'tickets', 'user','id')
        read_only_fields = ('id','user',)

class TicketListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TicketList
        fields=('title', 'content', 'tickets', 'user')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('ticketlist','user',)

class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'