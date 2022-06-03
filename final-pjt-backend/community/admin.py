from django.contrib import admin
from .models import Review, Comment
# Register your models here.

admin.site.register(Comment)
admin.site.register(Review)