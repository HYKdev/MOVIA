from rest_framework import serializers
from ..models import Image, Actor, Director


class ImageSerializer(serializers.ModelSerializer):
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
    class DirectorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'

    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Image
        fields = '__all__'