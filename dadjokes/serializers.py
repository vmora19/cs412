from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    '''
    A serializer for the Joke model.
    Specify which fields to send in the api.
    '''
    class Meta:
        model = Joke
        fields = ['id', 'text', 'name', 'timestamp']


class PictureSerializer(serializers.ModelSerializer):
    '''
    A serializer for the Picture model.
    Specify which fields to send in the api.
    '''
    class Meta:
        model = Picture
        fields = ['id', 'picture', 'name', 'timestamp']
