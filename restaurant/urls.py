# File: restaurant/urls.py
# Author: Valentina Mora (vmora19@bu.edu), 09/16/2025
# Description: Urls for restaurant application

from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.main_page, name='main_page'),
    path(r'main', views.main_page, name='main_page'),
    path(r'order', views.order_page, name='order_page'),
    path(r'confirmation', views.confirmation_page, name='confirmation_page')
]