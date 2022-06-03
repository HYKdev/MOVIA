from rest_framework import serializers
from django.contrib.auth import get_user_model

from community.models import Review
from ..models import Actor, Image, Movie

User = get_user_model()

class ActorListSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    class ImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = Image
            fields = '__all__'
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    movies = MovieSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Actor
        fields = '__all__'