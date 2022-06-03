from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movielist/', views.movie_list),
    path('moviedetail/<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/movielike/', views.like_movie),
    path('actorlist/', views.actor_list),
    path('actordetail/<int:actor_pk>/', views.actor_detail),
    path('<int:actor_pk>/actorlike/', views.like_actor),

]