# mini_insta/urls.py

from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import ShowAllView, ProfileView


urlpatterns = [
    # path(r'', RandomArticleView.as_view(), name="random"),
    path(r'show_all', ShowAllView.as_view(), name="show_all"), # modified
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'), # new
]