from django.db import models
from django.conf import settings
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=50)
    url = models.TextField()

class Actor(models.Model):
    name = models.CharField(max_length=100)
    main_image = models.TextField()
    images = models.ManyToManyField(Image, related_name='actors')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors')

class Director(models.Model):
    name = models.CharField(max_length=100)
    main_image = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.TextField()
    pubdate = models.CharField(max_length=10)
    userating = models.IntegerField()
    overview = models.TextField()
    trailer = models.TextField()
    directors = models.ManyToManyField(Director, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
