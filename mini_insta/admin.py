# File: mini_insta/admin.py
# Author: Valentina Mora (vmora19@bu.edu), 09/25/2025
# Description: Admin file where we import Profile

from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)