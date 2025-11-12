from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import random
from .models import Joke, Picture
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JokeSerializer, PictureSerializer



# Create your views here.
class RandomJokeView(DetailView):
    '''Displays a singular random joke.'''
    model = Joke
    template_name = "dadjokes/dadjoke.html"
    context_object_name = "joke" # note singular variable name

    # methods
    def get_object(self):
        '''return one instance of the Article object selected at random.'''

        all_jokes = Joke.objects.all()
        joke = random.choice(all_jokes)
        return joke
    
    def get_context_data(self, **kwargs):
        '''add a random Picture to the context.'''
        context = super().get_context_data(**kwargs)
        all_pictures = Picture.objects.all()
        context["picture"] = random.choice(all_pictures) if all_pictures else None
        return context
    

class ShowAllView(ListView):
    '''Define a view class to show all dad jokes.'''

    model = Joke
    template_name = "dadjokes/all_jokes.html"
    context_object_name = "jokes"

class JokeDetailView(DetailView):
    '''Display a single joke.'''

    model = Joke
    template_name = "dadjokes/show_joke.html"
    context_object_name = "joke" # note singular variable name

class ShowAllPicturesView(ListView):
    '''Define a view class to show all pictures.'''

    model = Picture
    template_name = "dadjokes/all_pictures.html"
    context_object_name = "pictures"

class PictureDetailView(DetailView):
    '''Display a single picture.'''

    model = Picture
    template_name = "dadjokes/show_picture.html"
    context_object_name = "picture" # note singular variable name

class RandomJokeAPI(APIView):
    '''An API view to return a randome Joke'''

    def get(self, request):
        all_jokes = Joke.objects.all()
        joke = random.choice(all_jokes)
        serializer = JokeSerializer(joke)
        return Response(serializer.data)
    

class JokeListAPI(APIView):
    '''An API view to return list of all Joke'''

    def get(self, request):
        jokes = Joke.objects.all()
        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JokeDetailAPI(APIView):
    '''An API view to return detail of a Joke'''

    def get(self, request, pk):
        try:
            joke = Joke.objects.get(pk=pk)
        except Joke.DoesNotExist:
            return Response({"error": "Joke not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = JokeSerializer(joke)
        return Response(serializer.data)
    

class PictureListAPI(APIView):
    '''An API view to return all Pictures'''

    def get(self, request):
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)
    

class PictureDetailAPI(APIView):
    '''An API view to return one Picture'''

    def get(self, request, pk):
        try:
            picture = Picture.objects.get(pk=pk)
        except Picture.DoesNotExist:
            return Response({"error": "Picture not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PictureSerializer(picture)
        return Response(serializer.data)
    

class RandomPictureAPI(APIView):
    '''An API view to return one random Picture'''
    
    def get(self, request):
        all_pictures = Picture.objects.all()
        if not all_pictures:
            return Response({"error": "No pictures available"}, status=status.HTTP_404_NOT_FOUND)
        picture = random.choice(all_pictures)
        serializer = PictureSerializer(picture)
        return Response(serializer.data)