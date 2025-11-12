# File: mini_insta/urls.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Url paths for mini_insta application

from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path(r'', RandomJokeView.as_view(), name="random"),
    path(r'random', RandomJokeView.as_view(), name="random"),
    path(r'jokes', ShowAllView.as_view(), name="all_jokes"),
    path(r'joke/<int:pk>', JokeDetailView.as_view(), name='show_joke'),
    path(r'pictures', ShowAllPicturesView.as_view(), name='all_pictures'),
    path(r'picture/<int:pk>', PictureDetailView.as_view(), name='show_picture'),
    path('api/', RandomJokeAPI.as_view(), name='api_root'),
    path('api/random', RandomJokeAPI.as_view(), name='api_random_joke'),
    path('api/jokes', JokeListAPI.as_view(), name='api_all_jokes'),
    path('api/joke/<int:pk>', JokeDetailAPI.as_view(), name='api_joke_detail'),
    path('api/pictures', PictureListAPI.as_view(), name='api_all_pictures'),
    path('api/picture/<int:pk>', PictureDetailAPI.as_view(), name='api_picture_detail'),
    path('api/random_picture', RandomPictureAPI.as_view(), name='api_random_picture'),
]