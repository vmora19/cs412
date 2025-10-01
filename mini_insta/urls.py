# File: mini_insta/urls.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Url paths for mini_insta application

from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import ProfileListView, ProfileDetailView, PostDetailView


urlpatterns = [
    path(r'', ProfileListView.as_view(), name="show_all_profiles"),
    path(r'show_all_profiles', ProfileListView.as_view(), name="show_all_profiles"), # modified
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'), # new
    path(r'post/<int:pk>', PostDetailView.as_view(), name='show_post'),
]