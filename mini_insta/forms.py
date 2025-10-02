# File: mini_insta/forms.py
# Author: Valentina Mora (vmora19@bu.edu), 09/30/2025
# Description: forms for mini_insta application

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to add an article to the database.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Post
        fields = ['caption']