from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Encapsulate the data of a Joke.'''

    # define the data attributes of the Joke object
    text = models.TextField(blank=True)
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.text} by: {self.name}'
    

class Picture(models.Model):
    '''Encapsulate the data of a Picture.'''

    # define the data attributes of the Picture object
    picture = models.URLField(blank=True)
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
