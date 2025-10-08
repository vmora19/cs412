# File: mini_insta/urls.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Url paths for mini_insta application

from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import *


urlpatterns = [
    path(r'', ProfileListView.as_view(), name="show_all_profiles"),
    path(r'show_all_profiles', ProfileListView.as_view(), name="show_all_profiles"),
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),
    path(r'post/<int:pk>', PostDetailView.as_view(), name='show_post'),    
    path(r'profile/<int:pk>/create_post', CreatePostView.as_view(), name="create_post"),
    path(r'profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path(r'post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path(r'post/<int:pk>/update', UpdatePostView.as_view(), name="update_post")
]