# mini_insta/urls.py

from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import ProfileListView


urlpatterns = [
    # path(r'', RandomArticleView.as_view(), name="random"),
    path(r'show_all_profiles', ProfileListView.as_view(), name="show_all_profiles"), # modified
    # path('profile/<int:pk>', ProfileView.as_view(), name='profile'), # new
]