# File: quotes/urls.py
# Author: Valentina Mora (vmora19@bu.edu), 09/11/2025
# Description: Urls for quotes application

from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home_page, name='home_page'),
    path(r'quote', views.quote_page, name='quote_page'),
    path(r'show_all', views.show_all_page, name='show_all_page'),
    path(r'about', views.about_page, name='about_page')
]