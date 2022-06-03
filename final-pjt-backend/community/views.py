from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count
from .models import Comment, Review
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers.review import ReviewSerializer, ReviewListSerializer
from .serializers.comment import CommentSerializer
from movies.models import Actor
# Create your views here.


@api_view(['GET', 'POST'])
def review_list_create(request):
    user = request.user
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()

@api_view(['POST'])
def create_comment(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)
 
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()