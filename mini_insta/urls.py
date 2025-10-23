# File: mini_insta/urls.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Url paths for mini_insta application

from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path(r'', ProfileListView.as_view(), name="show_all_profiles"),
    path(r'show_all_profiles', ProfileListView.as_view(), name="show_all_profiles"),
    path(r'profile/<int:pk>/', ProfileDetailView.as_view(), name='show_profile'),
    path(r'post/<int:pk>', PostDetailView.as_view(), name='show_post'),    
    path(r'profile/create_post', CreatePostView.as_view(), name="create_post"),
    path(r'profile/update', UpdateProfileView.as_view(), name="update_profile"),
    path(r'post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path(r'post/<int:pk>/update', UpdatePostView.as_view(), name="update_post"),
    path(r'profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name="show_followers"),
    path(r'profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name="show_following"),
    path(r'profile/feed', PostFeedListView.as_view(), name="show_feed"),
    path(r'profile/search', SearchView.as_view(), name="show_search"),
    path('login/', auth_views.LoginView.as_view(template_name="mini_insta/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_insta/logged_out.html'), name="logout_confirmation"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),
]