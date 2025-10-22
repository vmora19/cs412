# blog/views.py
# views for the blog application
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Comment
from .forms import CreateArticleForm, UpdateArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.urls import reverse


# Create your views here.
class ShowAllView(ListView):
    '''Define a view class to show all blog Articles.'''

    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles"

    def dispatch(self, request, *args, **kwargs):
        '''override the dispatch method to add debugging information'''

        if request.user.is_authenticated:
            print(f'ShowAllView.dispatch(): request.user={request.user}')
        else:
            print(f'ShowAllView.dispatch(): not logged in.')
        return super().dispatch(request, *args, **kwargs)

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
    

#define a subclass of CreateView to handle creation of Article objects
class CreateArticleView(LoginRequiredMixin, CreateView):
    '''A view to handle creation of a new Article.
    (1) Display the html form to the user (GET)
    (2) Process form submission and store the new article object (POST)
    '''

    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"

    def get_login_url(self):
        '''return the url for this app's login page'''
        return reverse('login')

    def form_valid(self, form):
        '''validating a form'''

        #print out the form data
        print(f'CreateArticleView.form_valid(): {form.cleaned_data}')

        user = self.request.user
        print(f'CreateArticleView.form_valid(): {user}')
        form.instance.user = user

        #delegate work to the superclass to do the rest:
        return super().form_valid(form)
    
class UpdateArticleView(UpdateView):
    '''View class to handle update of an article instance.'''
    model=Article
    form_class = UpdateArticleForm
    template_name="blog/update_article_form.html"


class DeleteCommentView(DeleteView):
    '''View class to handle the deletion of a comment.'''

    model = Comment
    template_name = "blog/delete_comment_form.html"

    def get_success_url(self):
        '''Return the URL to redirect to after a successful delete.'''

        # return super().get_success_url()
        pk = self.kwargs['pk']

        #find the Comment object:
        comment = Comment.objects.get(pk=pk)

        article = comment.article

        return reverse('article', kwargs = {'pk':article.pk})
