# File: mini_insta/views.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Views for the mini_insta application

from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, Post, Photo, Follow, Like
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm, CreateFollowForm, DeleteFollowForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy




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

    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        is_following = False

        if self.request.user.is_authenticated and self.request.user != profile.user:
            follower_profile = Profile.objects.get(user=self.request.user)
            is_following = Follow.objects.filter(
                follower_profile=follower_profile,
                profile=profile
            ).exists()

        context["is_following"] = is_following
        return context

class PostDetailView(DetailView):
    '''Display a single post.'''

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post" # note singular variable name

    def get_context_data(self, **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        user = self.request.user
        context["photos"] = post.get_all_photos()  # explicitly call the method
        if user.is_authenticated:
            current_profile = get_object_or_404(Profile, user=user)
            context["current_profile"] = current_profile
            context["has_liked"] = post.get_likes().filter(profile=current_profile).exists()
        else:
            context["current_profile"] = None
            context["has_liked"] = False
        return context

#define a subclass of CreateView to handle creation of Post objects
class CreatePostView(LoginRequiredMixin, CreateView):
    '''A view to handle creation of a new Post.
    (1) Display the html form to the user (GET)
    (2) Process form submission and store the new post object (POST)
    '''

    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_object(self):
        '''return one instance of the Profile object.'''
        return get_object_or_404(Profile, user=self.request.user)

    def get_login_url(self):
        '''return the url for this app's login page'''
        return reverse('login')
    
    def get_context_data(self, **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context
    
    def form_valid(self, form):
        '''validate incoming create post form'''
        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile
        response = super().form_valid(form)

        files = self.request.FILES.getlist('files')
        if files:
            for file in files:
                Photo.objects.create(post=self.object, image_file=file)

        return response
    
    def get_success_url(self):
        '''redirect to the new Post’s detail page'''
        return reverse("show_post", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        '''handle the cancel button'''
        if "cancel" in request.POST:
            return redirect("show_profile", pk=self.kwargs['pk'])
        return super().post(request, *args, **kwargs)
    

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    '''a view to handle the update of a profile.'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def get_object(self):
        '''return one instance of the Profile object.'''
        return get_object_or_404(Profile, user=self.request.user)

    def get_login_url(self):
        '''return the url for this app's login page'''
        return reverse('login')

    def get_success_url(self):
        # redirect to the new profile page
        return reverse("show_profile", kwargs={"pk": self.object.pk})
    

class DeletePostView(LoginRequiredMixin, DeleteView):
    '''a view to handle the deletion of a post.'''
    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_login_url(self):
        '''return the url for this app's login page'''
        return reverse('login')

    def get_context_data(self,  **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        profile = post.profile
        context['post'] = post
        context['profile'] = profile
        return context
    
    def get_success_url(self):
        '''redirect to the deleted post's corresponding profile detail page.'''
        return reverse("show_profile", kwargs={"pk": self.object.profile.pk})
    

class UpdatePostView(LoginRequiredMixin, UpdateView):
    '''a view to handle updating a post.'''
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_object(self):
        '''return one instance of the Post object.'''
        return get_object_or_404(Post, pk=self.kwargs["pk"])

    def get_login_url(self):
        '''return the url for this app's login page'''
        return reverse('login')

    def get_context_data(self,  **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        profile = post.profile
        caption = post.caption
        context['post'] = post
        context['caption'] = caption
        context['profile'] = profile
        return context
    
    def get_success_url(self):
        '''redirect to the deleted post's corresponding profile detail page.'''
        return reverse("show_post", kwargs={"pk": self.object.pk})
    

class ShowFollowersDetailView(DetailView):
    '''a view to handle displaying followers'''
    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "profile"

    def get_context_data(self,  **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['followers'] = profile.get_followers()
        context['num_followers'] = profile.get_num_followers()
        return context
    
class ShowFollowingDetailView(DetailView):
    '''a view to handle displaying following'''
    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = "profile"

    def get_context_data(self,  **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context["following"] = profile.get_following()
        context["num_following"] = profile.get_num_following()
        return context
    

class PostFeedListView(ListView):
    '''a view to handle displaying the post feed of a given profile'''
    model = Post
    template_name = "mini_insta/show_feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        '''Return the posts in the feed for this profile.'''
        profile = get_object_or_404(Profile, user=self.request.user)
        return profile.get_post_feed()

    def get_context_data(self, **kwargs):
        '''Add the current profile to the context.'''
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, user=self.request.user)
        return context
    
    def get_success_url(self):
        '''redirect to the profile's feed page'''
        return reverse("show_feed", kwargs={"pk": self.object.profile.pk})
    

class SearchView(ListView):
    '''a view to handle searching for profiles and posts'''

    model = Profile
    template_name = "mini_insta/search_results.html"
    context_object_name = "profiles"

    def dispatch(self, request, *args, **kwargs):
        '''if no query render template form, otherwise return dispatch'''
        if "q" not in self.request.GET:
            profile = get_object_or_404(Profile, user=self.request.user)
            return render(request, "mini_insta/search.html", {"profile": profile})
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        '''return posts which match the query'''
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(caption__icontains=query)
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        '''add profile, query, posts, and matching profiles to context'''
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        profile = get_object_or_404(Profile, pk=self.kwargs["pk"])

        posts = self.get_queryset()

        matching_profiles = Profile.objects.filter(
            Q(username__icontains=query)
            | Q(display_name__icontains=query)
            | Q(bio_text__icontains=query)
        )

        context["profile"] = profile
        context["query"] = query
        context["posts"] = posts
        context["profiles"] = matching_profiles
        return context
    
class CreateProfileView(CreateView):
    '''A view for handling creating a profile.'''
    model = Profile
    template_name = "mini_insta/create_profile_form.html"
    fields = ['username', 'display_name', 'profile_image_url', 'bio_text']

    def get_context_data(self, **kwargs):
        ''''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm()
        return context
    
    def form_valid(self, form):
        '''validate incoming create profile form'''
        user_form = UserCreationForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            form.instance.user = user
            return super().form_valid(form)
        else:
            context = self.get_context_data(form=form)
            context['user_form'] = user_form
            return self.render_to_response(context)
    
    def get_success_url(self):
        '''redirect to the Profile's detail page'''
        return reverse('show_profile')
    
class CreateFollowView(LoginRequiredMixin, CreateView):
    '''class for handling a profile following another profile'''
    
    model = Follow
    form_class = CreateFollowForm
    template_name = "mini_insta/follow_form.html"
    
    def get_login_url(self):
        '''return the url for this app's login page'''
        return reverse('login')
    
    def get_context_data(self, **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        profile_to_follow = get_object_or_404(Profile, pk=self.kwargs["pk"])
        follower_profile = get_object_or_404(Profile, user=self.request.user)

        context["profile"] = profile_to_follow
        context["follower_profile"] = follower_profile
        return context
    
    def form_valid(self, form):
        '''Set the follower and followed profiles before saving.'''
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs["pk"])
        form.instance.follower_profile = get_object_or_404(Profile, user=self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        '''redirect to the new followed profile's detail page'''
        return reverse("show_profile", kwargs={"pk": self.object.profile.pk})
    

class DeleteFollowView(LoginRequiredMixin, DeleteView):
    '''a view to handle the deletion of a follow relationship.'''
    model = Follow
    template_name = "mini_insta/delete_follow_form.html"
    form_class = DeleteFollowForm

    def get_login_url(self):
        '''return the url for this app's login page'''
        return reverse('login')
    
    def get_object(self, queryset=None):
        '''return the follow object between the current user and target profile.'''
        profile_to_unfollow = get_object_or_404(Profile, pk=self.kwargs["pk"])
        follower_profile = get_object_or_404(Profile, user=self.request.user)

        return get_object_or_404(
            Follow,
            profile=profile_to_unfollow,
            follower_profile=follower_profile
        )
    
    def get_context_data(self,  **kwargs):
        '''override the built in get_context_data to populate fields.'''
        context = super().get_context_data(**kwargs)
        profile_to_unfollow = get_object_or_404(Profile, pk=self.kwargs["pk"])
        follower_profile = get_object_or_404(Profile, user=self.request.user)
        context["profile"] = profile_to_unfollow
        context["follower_profile"] = follower_profile
        return context
    
    def get_success_url(self):
        '''redirect to the corresponding profile detail page that was unfollowed.'''
        return reverse("show_profile", kwargs={"pk": self.object.profile.pk})


class LikeDetailView(LoginRequiredMixin, CreateView):
    '''a view to handle liking a post.'''
    model = Like

    def post(self, request, *args, **kwargs):
        '''method for creating the like object'''
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        profile = get_object_or_404(Profile, user=request.user)

        if post.profile != profile:
            Like.objects.get_or_create(post=post, profile=profile)

        return redirect("show_post", pk=post.pk)
    
class LikeDeleteView(LoginRequiredMixin, DeleteView):
    '''a view to handle unliking a post.'''
    model = Like

    def post(self, request, *args, **kwargs):
        '''method for deleting the like object'''
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        profile = get_object_or_404(Profile, user=request.user)
        like = Like.objects.filter(post=post, profile=profile).first()
        if like:
            like.delete()
        return redirect("show_post", pk=post.pk)


