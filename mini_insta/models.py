# File: mini_insta/models.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Models for mini_insta application in which
# you can create a profile with username, display_name, profile_image_url, bio_text, join_date

from django.db import models

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
        return f'{self.username} by: {self.display_name}'
