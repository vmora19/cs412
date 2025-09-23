# mini_insta/views.py
# views for the blog application
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
import random

# Create your views here.
class ProfileListView(ListView):
    '''Define a view class to show all insta Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

# class ProfileView(DetailView):
#     '''Display a single profile.'''

#     model = Profile
#     template_name = "mini_insta/profile.html"
#     context_object_name = "profile" # note singular variable name
