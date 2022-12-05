from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer, ReviewListSerializer
from .models import Review
from movies.models import Movie
from django.contrib.auth import get_user_model

@api_view(['POST'])
def create_review(request):
    # print(request.data)
    movie = get_object_or_404(Movie, id=request.data.get('movie_id'))
    user=get_object_or_404(get_user_model(), username=request.data.get('username'))
    newdata={
        'title':request.data.get('title'),
        'content':request.data.get('content'),
        'rate':request.data.get("rate")
    }
    serializer = ReviewSerializer(data=newdata)
    # print(serializer)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'review {review_pk} is deleted',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
