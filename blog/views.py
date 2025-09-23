# blog/views.py
# views for the blog application
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
import random

# Create your views here.
class ShowAllView(ListView):
    '''Define a view class to show all blog Articles.'''

    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles"

class ArticleView(DetailView):
    '''Display a single article.'''

    model = Article
    template_name = "blog/article.html"
    context_object_name = "article" # note singular variable name

class RandomArticleView(DetailView):
    '''Displays a singular random article.'''
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article" # note singular variable name

    # methods
    def get_object(self):
        '''return one instance of the Article object selected at random.'''

        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article