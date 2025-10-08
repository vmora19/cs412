# File: mini_insta/views.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Views for the mini_insta application

from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["photos"] = post.get_all_photos()  # explicitly call the method
        return context

#define a subclass of CreateView to handle creation of Post objects
class CreatePostView(CreateView):
    '''A view to handle creation of a new Post.
    (1) Display the html form to the user (GET)
    (2) Process form submission and store the new post object (POST)
    '''

    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(pk=self.kwargs["pk"])
        return context
    
    def form_valid(self, form):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form.instance.profile = profile
        response = super().form_valid(form)

        files = self.request.FILES.getlist('files')
        if files:
            for file in files:
                Photo.objects.create(post=self.object, image_file=file)

        return response
    
    def get_success_url(self):
        # redirect to the new Post’s detail page
        return reverse("show_post", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        # handle the cancel button
        if "cancel" in request.POST:
            return redirect("show_profile", pk=self.kwargs['pk'])
        return super().post(request, *args, **kwargs)
    

class UpdateProfileView(UpdateView):
    '''a view to handle the update of a profile.'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def get_success_url(self):
        # redirect to the new profile page
        return reverse("show_profile", kwargs={"pk": self.object.pk})
