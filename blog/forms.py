# blog/forms.py
# define the forms that we use for create/update/delete operations

from django import forms
from .models import Article

class CreateArticleForm(forms.ModelForm):
    '''A form to add an article to the database.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Article
        fields = ['author', 'title', 'text', 'image_file']


class UpdateArticleForm(forms.ModelForm):
    '''A form to update an article in the database.'''

    class Meta:
        '''associate this form with a model in our database.'''
        model = Article
        fields = ["title", "text"] # which fields we can update