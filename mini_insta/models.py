# File: mini_insta/models.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Models for mini_insta application in which
# you can create a profile with username, display_name, profile_image_url, bio_text, join_date

from django.db import models
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data of an insta Profile.'''

    # define the data attributes of the Article object
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.username}: {self.display_name}'
    
    def get_all_posts(self):
        '''Return a queryset of posts about this Profile.'''
        posts = Post.objects.filter(profile=self)
        return posts
    
class Post(models.Model):
    '''Encapsulate the data of an insta Post.'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #foreign key
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.profile} {self.caption}'
    
    def get_all_photos(self):
        '''Return a queryset of photos about this Post.'''
        photos = Photo.objects.filter(post=self)
        return photos
    
    def get_first_photo(self):
        '''Return the first photo of this Post or None if no photo.'''
        photos = Photo.objects.filter(post=self).first()
        return photos
    
    def get_absolute_url(self):
        '''Return a url to display one instance of this object.'''
        return reverse('post', kwargs={'pk':self.pk})
    

class Photo(models.Model):
    '''Encapsulate the data attributes of an image associated with a Post.'''

    post = models.ForeignKey(Post, on_delete=models.CASCADE) #foreign key
    image_url = models.URLField(blank=True) 
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.post}'

