# File: project/models.py
# Author: Valentina Mora (vmora19@bu.edu), 11/22/2025
# Description: models for project application

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data of a Profile.'''

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="financial_profile")
    display_name = models.CharField(max_length=100, blank=True)
    bio_text = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        if self.user:
            return self.user.username
        return "Unassigned Profile"

class Category(models.Model):
    '''Encapsulate the data of categories a user creates '''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #foreign key
    category_name = models.CharField(max_length=100)

    def __str__(self):
        '''string representation of Category model.'''
        return f"{self.category_name}"

class Note(models.Model):
    '''Encapsulate the data of a User's Notes'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #foreign key
    title_text = models.TextField(blank=True)
    note_text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)

class Account(models.Model):
    '''Encapsulate the data of a user's bank account'''

    CARD_CHOICES = [
        ("credit", "Credit"),
        ("debit", "Debit"),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #foreign key
    bank = models.TextField(blank=True)
    card_type = models.CharField(max_length=10, choices=CARD_CHOICES)
    card_num = models.IntegerField(blank=True)
    total_spent = models.DecimalField(max_digits=9, decimal_places=2)
    remaining_money = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        '''string representation of Account model.'''
        return f"{self.bank} — {self.card_type.capitalize()} ••••{str(self.card_num)[-4:]}"

class Transaction(models.Model):
    '''Encapsulate the data of a user's transactions '''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #foreign key
    account = models.ForeignKey(Account, on_delete=models.CASCADE) #foreign key
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #foreign key
    amount = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        '''string representation of Transaction'''
        return f"{self.profile.display_name} spent ${self.amount} on {self.description}"

