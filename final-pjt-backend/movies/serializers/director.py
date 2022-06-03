from rest_framework import serializers
from ..models import Director, Image, Movie


class DirectorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Director
        fields = '__all__'