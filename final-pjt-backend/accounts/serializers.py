from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Actor, Movie
from community.models import Review, Comment

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = '__all__'
    
    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = '__all__'

    class CommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = '__all__'

    like_actors = ActorSerializer(many=True, read_only=True)
    like_movies = MovieSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = User
        fields = ('pk', 'username', 'like_actors', 'like_movies', 'reviews', 'comments')