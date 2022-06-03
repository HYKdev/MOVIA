from django.contrib import admin
from .models import Movie, Actor, Genre, Director, Image
# Register your models here.

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Image)
