# file: hw/views.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time

# Create your views here.

def home(request):
    '''Func to respond to the home request.'''

    response_text = f'''
    <html>
    <h1>Hello, world!</h1>
    The current time is {time.ctime()}
    </html>
    '''

    return HttpResponse(response_text)


def home_page(request):
    '''Respond to the url '', delegate work to a template.'''

    template_name = 'hw/home.html'

    context = {
        "time": time.ctime()
    }
    return render(request, template_name, context)

def about_page(request):
    '''Respond to the url 'about', delegate work to a template.'''

    template_name = 'hw/about.html'

    context = {
        "time": time.ctime()
    }
    return render(request, template_name, context)