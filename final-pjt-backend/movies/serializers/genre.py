from rest_framework import serializers
from ..models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            field = '__all__'

    movies = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Genre
        fields = '__all__'