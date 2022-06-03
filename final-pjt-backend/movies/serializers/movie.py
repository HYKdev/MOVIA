from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Actor, Director, Genre, Movie

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
    class DirectorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = '__all__'
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'