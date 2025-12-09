# File: project/forms.py
# Author: Valentina Mora (vmora19@bu.edu), 12/01/2025
# Description: forms for project application

from django import forms
from .models import *

class CreateTransactionForm(forms.ModelForm):
    '''A form to add a transaction to the database.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Transaction
        fields = ['account', 'category', 'amount', 'description' ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        profile = Profile.objects.get(user=user)
        self.fields['account'].queryset = Account.objects.filter(profile=profile)
        self.fields['category'].queryset = Category.objects.filter(profile=profile)


class CreateCategoryForm(forms.ModelForm):
    '''A form to add a category to the database.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model= Category
        fields=['category_name']

class CreateNoteForm(forms.ModelForm):
    '''A form to add a note in the database.'''

    class Meta:
        '''associate this form with a mofrl from our database.'''
        model = Note
        fields=['title_text', 'note_text']

class CreateProfileForm(forms.ModelForm):
    '''A form to create a profile.'''

    class Meta:
        '''assocate this form with a model from our database.'''
        model = Profile
        fields = ['user', 'display_name', 'bio_text', 'profile_image_url']

class CreateAccountForm(forms.ModelForm):
    '''A form to create an account.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Account
        fields = ['bank', 'card_type', 'card_num', 'total_spent', 'remaining_money']

class UpdateTransactionForm(forms.ModelForm):
    '''A form to update a transaction.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Transaction
        fields = ['account', 'category', 'amount', 'description' ]

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a Profile.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Profile
        fields = ['display_name', 'bio_text', 'profile_image_url']

class DeleteTransactionForm(forms.ModelForm):
    '''A form to delete a transaction.'''

    class Meta:
        '''associate this form with a model from our databse.'''
        model = Transaction
        fields = []

class UpdateNoteForm(forms.ModelForm):
    '''A form to update a Note.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Note
        fields = ['title_text', 'note_text']

