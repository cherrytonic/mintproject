from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import UserSerializer, UserFollowSerializer, getUserSerializer
from django.views.decorators.http import require_http_methods, require_POST, require_GET


@api_view(['POST'])
def signup(request):
    data=request.data
    # print(data)
    if data['password1']!=data['password2']:
        return Response({'error':'비밀번호가 일치하지 않습니다.'},status.HTTP_400_BAD_REQUEST)
    else:
        newdata={
            'username':data['username'],
            'password':data['password1'],
            'nickname':data.get('nickname'),
            'genre_preference':data.get('genre_preference'),
        }
        serializer=UserSerializer(data=newdata)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            #사용자의 암호를 해쉬함수를 통해 바꿔줌(암호화)
            user.set_password(newdata.get('password'))
            user.save()
            return Response(serializer.data,status.HTTP_201_CREATED)

@api_view(['POST'])
def follow(request, username):
        User = get_user_model()
        me = request.user
        you = User.objects.get(username=username)
        if me != you:
            # 내가(request.user) 그 사람의 팔로워 목록에 있다면
            # if me in you.followers.all():
            if you.followers.filter(username=me).exists():
                # 언팔로우
                print('unfollowed')
                you.followers.remove(me)
                is_follewed = False
            else:
                # 팔로우
                print('followed')
                you.followers.add(me)
                is_follewed = True
            # 화면에 필요한 data 생성
            context = {
                "is_followed": is_follewed,
                "followers_count": you.followers.count(),
                "followings_count": you.followings.count(),
            }
            # 화면에 필요한 data 만 담아서 응답, html 등 은 처리하지 않음
            return JsonResponse(context)

@api_view(['GET',"POST"])
def getUserData(request,username):
    person=get_user_model().objects.get(username=username)
    follow_list=[]
    for p in list(person.followers.all()):
        follow_list.append(str(p))
    print(follow_list)
    if request.method=="GET":
        data={
            'username':person.username,
            'nickname':person.nickname,
            'genre_preference':person.genre_preference,
            'followings_count':person.followings.count(),
            'followers_count':person.followers.count(),
            'follow_list': follow_list,
            'id' : person.id
        }
        # serializer=getUserSerializer(person)
        return JsonResponse(data, status=status.HTTP_200_OK)
    
    else:
        print(request.data)
        data={
            'username':person.username,
            'nickname':person.nickname,
            'genre_preference':person.genre_preference,
            'followings_count':person.followings.count(),
            'followers_count':person.followers.count(),
            'is_followed':True if person.followers.filter(username=request.data.requestUser).exists() else False
        }
        # serializer=getUserSerializer(person)
        return JsonResponse(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getUser(request,user_pk):
    # print('pk=',user_pk)
    person=get_user_model().objects.get(pk=user_pk)
    # print(person)
    serializer=UserSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllUser(request):
    print(111111)
    # print('pk=',user_pk)
    person=get_user_model().objects.all()
    # print(person)
    serializer=UserSerializer(person,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)