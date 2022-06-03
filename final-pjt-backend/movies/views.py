from django.shortcuts import get_object_or_404, get_list_or_404
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Actor, Movie
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.actor import ActorListSerializer, ActorSerializer
from pprint import pprint
import random
# Create your views here.
# https://openapi.naver.com/v1/search/movie.json
# ?query={검색내용}&display={출력건수(int)}&start={검색의 시작위치}&genre=1
# 1: 드라마 2: 판타지 3: 서부 4: 공포 5: 로맨스 6: 모험 7: 스릴러 8: 느와르 9: 컬트 10: 다큐멘터리 11: 코미디 12: 가족 13: 미스터리
# 14: 전쟁 15: 애니메이션 16: 범죄 17: 뮤지컬 18: SF 21: 에로 22: 서스펜스 23: 서사 24: 블랙코미디 25: 실험 26: 영화카툰 27: 영화음악 28: 영화패러디포스터

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        actors_list = get_list_or_404(Actor)
        actors = random.sample(actors_list, 4)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie,pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Actor)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    if request.method == 'GET':
        actor = get_object_or_404(Actor,pk=actor_pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def like_actor(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    user = request.user
    if actor.like_users.filter(pk=user.pk).exists():
        actor.like_users.remove(user)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    else:
        actor.like_users.add(user)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)



@api_view(['GET'])
def movie_list1(request):
    if request.method == 'GET':
        client_id = "Mseg6pXGsBBO38xA8tHP"
        client_secret = "hPiCxtbpQO"
        movie = '어벤져스'
        header_parms = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret
        }
        url = f"https://openapi.naver.com/v1/search/movie.json?query={movie}"
        res = requests.get(url, headers=header_parms)
        data = res.json()
        datalist = []
        n = len(data['items'])
        for i in range(n):
            image = data['items'][i]['image']
            title = data['items'][i]['title']
            link = data['items'][i]['link']
            # pubDate = data['items'][i]['pubDate']
            # director = data['items'][i]['director'].split('|')[0]
            # actors = data['items'][i]['actor'].split('|')[:-1]
            # rating = float(data['items'][i]['userRating'])
        
            html = urlopen(link)
            bsObject = BeautifulSoup(html, "html.parser")
            # overview = ' '.join(bsObject.find('p', class_='con_tx').get_text().split())
            genres = []
            objgenres = bsObject.find('p', class_='info_spec').find('span').find_all('a')
            for item in objgenres:
                genres.append(item.get_text())

        # director_image = bsObject.find('p', class_='people').find('li')

            context = {
                'title': title,
                'link': link,
                'genres': genres,
                'image': image,
                # 'pubDate': pubDate,
                # 'director': director,
                # 'actors': actors,
                # 'rating': rating,
                # 'overview': overview,
                # 'director_image': director_image,
                # 'actor_image': actro_image,
            }
            datalist.append(context)
        return Response(datalist)

@api_view(['GET'])
def movie_detail1(request, movie_name):
    if request.method == 'GET':
        client_id = "Mseg6pXGsBBO38xA8tHP"
        client_secret = "hPiCxtbpQO"
        movie = movie_name
        header_parms = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret
        }
        url = f"https://openapi.naver.com/v1/search/movie.json?query={movie}"
        res = requests.get(url, headers=header_parms)
        data = res.json()

        image = data['items'][0]['image']
        title = data['items'][0]['title']
        link = data['items'][0]['link']
        pubDate = data['items'][0]['pubDate']
        director = data['items'][0]['director'].split('|')[0]
        actors = data['items'][0]['actor'].split('|')[:-1]
        rating = float(data['items'][0]['userRating'])

        html = urlopen(link)
        bsObject = BeautifulSoup(html, "html.parser")
        overview = ' '.join(bsObject.find('p', class_='con_tx').get_text().split())
        genres = []
        objgenres = bsObject.find('p', class_='info_spec').find('span').find_all('a')
        for item in objgenres:
            genres.append(item.get_text())
        
        # youtube_url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=25&key=AIzaSyA1IvoD6CLeYQZDVWlgkTFLdZjt0OPJQyk'
        
        
        # director_image = bsObject.find('p', class_='people').find('li')

        context = {
            'title': title,
            'link': link,
            'pubDate': pubDate,
            'director': director,
            'actors': actors,
            'rating': rating,
            'overview': overview,
            'genres': genres,
            'image': image,

            # 'director_image': director_image,
            # 'actor_image': actro_image,
        }
        return Response(context)

@api_view(['POST'])
def movie_create(request):
    if request.method == 'POST' and request.user == 'admin':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def movie_update_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass



