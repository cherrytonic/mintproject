from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .serializers import TicketListListSerializer,TicketListSerializer, CommentSerializer, CommentListSerializer
from .models import TicketList, Comment
from django.contrib.auth import get_user_model

@api_view(['GET'])
def getticketlists(request):
    ticketlists=TicketList.objects.all()
    serializer=TicketListListSerializer(ticketlists,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createticketlist(request):
    newticketlist=request.data
    user=get_object_or_404(get_user_model(), username=request.data.get('username'))
    newdata={
        'title':newticketlist.get('ticketListName'),
        'content':newticketlist.get('content'),
        'tickets':newticketlist.get('selectedTickets'),
    }
    # print(newdata,user)
    serializer=TicketListSerializer(data=newdata)
    # print(serializer)
    # print('qweqwe')
    if serializer.is_valid(raise_exception=True):
        # print('qweqwe')
        # print(123)
        serializer.save(user=user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def getticketlist(request,ticketlist_pk):
    ticketlist=TicketList.objects.get(pk=ticketlist_pk)
    if request.method=='GET':
        serializer=TicketListListSerializer(ticketlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        ticketlist.delete()
        return Response({'message':'Deleted'},status=status.HTTP_204_NO_CONTENT)
    else:
        newticketlist=request.data
        user=get_object_or_404(get_user_model(), username=request.data.get('username'))
        # print(user)
        newdata={
        'title':newticketlist.get('ticketListName'),
        'content':newticketlist.get('content'),
        'tickets':newticketlist.get('selectedTickets'),
        }
        serializer=TicketListListSerializer(ticketlist,data=newdata)
        # print(1231321321321)
        if serializer.is_valid(raise_exception=True):
            # print(user)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def createcomment(request,ticketlist_pk):
    # print(request.data)
    ticketlist=TicketList.objects.get(pk=ticketlist_pk)
    user=get_object_or_404(get_user_model(), username=request.data.get('username'))
    content=request.data.get('content')
    print(request.user,content)
    serializer=CommentSerializer(data={'content':content})
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, ticketlist=ticketlist)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getcomment(request,ticketlist_pk):
    comments=Comment.objects.all()
    serializer=CommentListSerializer(comments, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def likes(request,ticketlist_pk):
    # print(request.data)
    ticketlist=TicketList.objects.get(pk=ticketlist_pk)
    user=get_object_or_404(get_user_model(), pk=request.data.get('user'))
    # print(ticketlist,user)
    if ticketlist.like_users.filter(pk=request.data.get('user')).exists():
        ticketlist.like_users.remove(user)
        is_liked=False
    else:
        ticketlist.like_users.add(user)
        is_liked=True
    context={
        'is_liked':is_liked,
        'like_count':ticketlist.like_users.count()
    }
    return JsonResponse(context, status=status.HTTP_200_OK)

@api_view(['GET'])
def getlikes(request,ticketlist_pk,username):
    # print(request.data)
    ticketlist=TicketList.objects.get(pk=ticketlist_pk)
    # user=get_object_or_404(get_user_model(), username=username)
    # print(ticketlist,user)
    if ticketlist.like_users.filter(username=username).exists():
        is_liked=True
    else:
        is_liked=False
    context={
        'is_liked':is_liked,
        'like_count':ticketlist.like_users.count()
    }
    return JsonResponse(context, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deletecomment(request,ticketlist_pk,comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return Response({'message':'Deleted'},status=status.HTTP_204_NO_CONTENT)