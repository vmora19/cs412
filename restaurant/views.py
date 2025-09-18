# File: restaurant/views.py
# Author: Valentina Mora (vmora19@bu.edu), 09/16/2025
# Description: Views for restaurant application

from django.http import HttpResponse
from django.shortcuts import render
import random
import time
from datetime import datetime, timedelta

entree_prices = {
    "Pad Thai $13": 13,
    "Pad See Ew $14": 14,
    "Tom Yum Pad Thai $14": 14,
    "Pad Woon Sen $12": 12,
    "Sub Beef $2": 2,
    "Sub Shrimp $2": 2
}

specials = ["Miso Soup $10", "Tum Yum Soup $10", "Tom Kah Soup $10"]
special_of_the_day = specials[random.randint(0, len(specials) - 1)]

def main_page(request):
    '''Respond to the url 'main.html' and '', delegate work to a template.'''

    template_name = 'restaurant/main.html'

    context = {
        "time": time.ctime(),
        "picture_link": "nud-pob.webp"
    }

    return render(request, template_name, context)

def order_page(request):
    '''Respond to the url 'order.html', delegate work to a template.'''

    template_name = 'restaurant/order.html'
    specials = ["Miso Soup $10", "Tum Yum Soup $10", "Tom Kah Soup $10"]

    context = {
        "time": time.ctime(),
        "special": special_of_the_day
    }

    return render(request, template_name, context)

def confirmation_page(request):
    '''Process the form submission, and generate a result.'''

    
    print(request.POST)

    if request.POST:

        template_name = 'restaurant/confirmation.html'

        # extract form fields into variables:
        selected_entrees = request.POST.getlist('entree')
        instructions = request.POST['instructions']
        name = request.POST['customer-name']
        phone = request.POST['customer-phone']
        email = request.POST['customer-email']

        total = 0
        for entree in selected_entrees:
            total += entree_prices[entree]

        special = request.POST.get('special')
        if special:
            total += 10
            selected_entrees.append(special_of_the_day)

        added_minutes = random.randint(30, 60)
        future_time = datetime.now() + timedelta(minutes=added_minutes)


        # create context variables for use in the template
        context = {
            "time": time.ctime(),
            'future_time': future_time,
            'selected_entrees': ', '.join(selected_entrees),
            'instructions': instructions,
            'total': total,
            'name': name,
            'phone': phone,
            'email': email
        }

        # delegate the response to the template, provide context variables
        return render(request, template_name=template_name, context=context)
    
    # default behavior: handle the GET request
    template_name = 'restaurant/order.html'

    return render(request, template_name)