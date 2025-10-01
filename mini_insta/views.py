# File: mini_insta/views.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Views for the mini_insta application

from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, Post
import random

# Create your views here.
class ProfileListView(ListView):
    '''Define a view class to show all insta Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''Display a single profile.'''

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile" # note singular variable name

class PostDetailView(DetailView):
    '''Display a single post.'''

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post" # note singular variable name
    
