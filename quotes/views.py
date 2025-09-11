# file: quotes/views.py

from django.http import HttpResponse
from django.shortcuts import render
import random
import time

oscar_wilde_quotes = [  "Most people are other people. Their thoughts are someone else’s opinions, \
                        their lives are mimicry, their passions a quotation.", "To live is the rarest \
                        thing in the world. Most people exist, that is all.", "Be yourself; everyone else \
                        is already taken."
                    ]

oscar_wilde_pictures = ["oscar-wilde-gloves.jpg", 
                        "oscar-wilde-profile.webp", 
                        "oscar-wilde-thinking.jpeg"
                        ]

def home_page(request):
    '''Respond to the url '', delegate work to a template.'''

    template_name = 'quotes/home.html'

    context = {
        "quote": oscar_wilde_quotes[random.randint(0, len(oscar_wilde_quotes) - 1 )],
        "picture_link": oscar_wilde_pictures[random.randint(0, len(oscar_wilde_pictures) - 1)],
        "time": time.ctime()
    }

    return render(request, template_name, context)

def quote_page(request):
    '''Respond to the url 'quote.html', delegate work to a template.'''

    template_name = 'quotes/quote.html'

    context = {
        "quote": oscar_wilde_quotes[random.randint(0, len(oscar_wilde_quotes) - 1 )],
        "picture_link": oscar_wilde_pictures[random.randint(0, len(oscar_wilde_pictures) - 1)],
        "time": time.ctime()
    }

    return render(request, template_name, context)

def show_all_page(request):
    '''Respond to the url 'show_all.html', delegate work to a template.'''

    template_name = 'quotes/show_all.html'

    context = {
        "quote1": oscar_wilde_quotes[0],
        "quote2": oscar_wilde_quotes[1],
        "quote3": oscar_wilde_quotes[2],
        "image1": oscar_wilde_pictures[0],
        "image2": oscar_wilde_pictures[1],
        "image3": oscar_wilde_pictures[2],
        "time": time.ctime()
    }

    return render(request, template_name, context)

def about_page(request):
    '''Respond to the url 'about_page.html', delegate work to a template.'''

    template_name = 'quotes/about.html'

    context = {
        "about": "Oscar Wilde was a famous author.",
        "time": time.ctime()
    }

    return render(request, template_name, context)