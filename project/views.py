# File: project/views.py
# Author: Valentina Mora (vmora19@bu.edu), 12/01/2025
# Description: views for project application

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, Category, Note, Account, Transaction
from .forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

# Transaction Views

class TransactionListView(LoginRequiredMixin, ListView):
    '''Define a view class to show all Transactions.'''

    model = Transaction
    template_name = "project/show_all_transactions.html"
    context_object_name = "transactions"

    def get_queryset(self):
        '''get the queryset of transactions for logged in user'''

        profile = self.request.user.financial_profile
        qs = Transaction.objects.filter(profile=profile)

        # query parameters
        category_id = self.request.GET.get("category")
        account_id = self.request.GET.get("account")

        if category_id:
            qs = qs.filter(category_id=category_id)
        if account_id:
            qs = qs.filter(account_id=account_id)

        return qs
    
    def get_context_data(self, **kwargs):
        '''override the built in get_context_data to populate fields.'''

        context = super().get_context_data(**kwargs)
        profile = self.request.user.financial_profile

        context["categories"] = Category.objects.filter(profile=profile)
        context["accounts"] = Account.objects.filter(profile=profile)

        context["selected_category"] = self.request.GET.get("category")
        context["selected_account"] = self.request.GET.get("account")

        return context

class CreateTransactionView(LoginRequiredMixin, CreateView):
    '''Define a view class to create a Transaction.
        (1) Display the html form to the user (GET)
        (2) Process form submission and store the new post object (POST)
    '''

    form_class = CreateTransactionForm
    template_name = "project/create_transaction_form.html"

    def form_valid(self, form):
        '''validate incoming create transaction form'''

        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile

        response = super().form_valid(form)

        account = form.instance.account
        account.total_spent += form.instance.amount
        account.remaining_money -= form.instance.amount
        account.save()

        return response
    
    def get_form_kwargs(self):
        '''get args for create transaction form'''

        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_success_url(self):
        '''redirection url for succesful transacrion creation.'''

        return reverse("show_all_transactions")


class UpdateTransactionView(LoginRequiredMixin, UpdateView):
    '''Define a view class to update a Transaction.'''

    model = Transaction
    form_class = UpdateTransactionForm
    template_name = "project/update_transaction_form.html"
    context_object_name = "transaction"

    def get_queryset(self):
        '''get queryset if it belongs to logged in user.'''
        return Transaction.objects.filter(profile__user=self.request.user)
    
    def form_valid(self, form):
        '''validate incoming update transaction form'''
        transaction = self.get_object()
        old_amount = transaction.amount
        new_amount = form.cleaned_data['amount']
        account = transaction.account

        diff = new_amount - old_amount

        account.total_spent += diff
        account.remaining_money -= diff
        account.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        '''redirection url for succesful transacrion update.'''

        return reverse("show_transaction", kwargs={"pk": self.object.pk})

class TransactionDetailView(DetailView):
    '''Define a view class to show the details of a Transaction.'''

    model = Transaction
    template_name = "project/show_transaction.html"
    context_object_name="transaction"

class DeleteTransactionView(LoginRequiredMixin, DeleteView):
    '''Define a view class to delete a Transaction.'''

    model = Transaction
    template_name = "project/delete_transaction_form.html"

    def get_queryset(self):
        '''get queryset of logged in user.'''

        return Transaction.objects.filter(profile__user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        '''update account details with transaction amounts'''

        transaction = self.get_object()
        account = transaction.account

        account.total_spent -= transaction.amount
        account.remaining_money += transaction.amount
        account.save()

        return super().delete(request, *args, **kwargs)
    
    def get_success_url(self):
        '''redirection url for succesful transacrion deletion.'''
        
        return reverse("show_all_transactions")

# Profile Views

class ProfileDetailView(DetailView):
    '''Define a view class to show the details of a Profile.'''

    model = Profile
    template_name = "project/show_profile.html"
    context_object_name= "profile"

class UpdateProfileView(UpdateView):
    '''Define a view class to update the details of a Profile.'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = "project/update_profile_form.html"
    context_object_name = "profile"
    
    def form_valid(self, form):
        '''validate incoming update profile form'''

        profile = form.save(commit=False)

        if profile.user is None:
            profile.user = self.request.user

        profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        '''redirect to the update profile's corresponding detail page.'''

        return reverse("show_profile", kwargs={"pk": self.object.pk})

# Note Views

class CreateNoteView(CreateView):
    '''Define a view class to create a Note.'''

    form_class = CreateNoteForm
    template_name = "project/create_note_form.html"

    def form_valid(self, form):
        '''validate incoming create note form'''

        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile  # Assign profile before saving
        return super().form_valid(form)

    def get_success_url(self):
        '''redirect to show all notes.'''

        return reverse("show_all_notes")

class NoteDetailView(DetailView):
    '''Define a view class to show the details  of a Note.'''

    model = Note
    template_name = "project/show_note.html"
    context_object_name= "note"

class NotesListView(ListView):
    '''Define a view class to show all Notes.'''

    model = Note
    template_name = "project/show_all_notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        '''get the queryset of notes of user who is logged in.'''

        return Note.objects.filter(profile__user=self.request.user)

class NotesDeleteView(DeleteView):
    '''Define a view class to delete a Note.'''

    model = Note
    template_name = "project/delete_note_form.html"

    def get_success_url(self):
        '''redirect to display all notes.'''

        return reverse("show_all_notes")

class NoteUpdateView(UpdateView):
    '''Define a view class to update a Note.'''

    model = Note
    form_class = UpdateNoteForm
    template_name = "project/update_note_form.html"
    context_object_name = "note"
    
    def get_success_url(self):
        '''redirect to the updated note's corresponding detail page.'''

        return reverse("show_note", kwargs={"pk": self.object.pk})

# Category Views
    
class CreateCategoryView(CreateView):
    '''Define a view clas to create a Category.'''

    form_class = CreateCategoryForm
    template_name = "project/create_category_form.html"

    def form_valid(self, form):
        '''validate incoming create category form'''

        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile
        return super().form_valid(form)
    
    def get_success_url(self):
        '''redirect to the dashboard page.'''

        return reverse("show_dashboard")

# Account Views
    
class AccountDetailView(DetailView):
    '''Define a view class to show the details of an Account.'''

    model = Account
    template_name = "project/show_account.html"
    context_object_name= "account"

class AccountListView(LoginRequiredMixin, ListView):
    '''Define a view class to show all Accounts.'''

    model = Account
    template_name = "project/show_all_accounts.html"
    context_object_name = "account"

    def get_queryset(self):
        '''get queryset of logged in user.'''

        return Account.objects.filter(profile__user=self.request.user)
    
class CreateAccountView(LoginRequiredMixin, CreateView):
    '''Define a view class to create an Account.'''

    form_class = CreateAccountForm
    template_name = "project/create_account_form.html"

    def form_valid(self, form):
        '''validate incoming create account form'''

        profile = Profile.objects.get(user=self.request.user)
        form.instance.profile = profile
        return super().form_valid(form)

    def get_success_url(self):
        '''redirect to the dashboard page.'''

        return reverse("show_dashboard")
    
# Authentication Views
    
class UserLoginView(LoginView):
    '''Define a view class to log in.'''

    template_name = "project/login.html"

    def get_success_url(self):
        '''redirect to the dashboard page.'''

        return reverse("show_dashboard")
    
def custom_logout_view(request):
    '''Define a custom logout view.'''
    logout(request)
    return redirect(reverse("login"))


# Dashboard view
class DashboardView(LoginRequiredMixin, ListView):
    '''Define a view class to display dashboard.'''

    template_name = "project/dashboard.html"
    context_object_name = "accounts"
    model = Account

    def get_queryset(self):
        '''get queryset of logged in user.'''

        return Account.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        '''override the built in get_context_data to populate fields.'''

        context = super().get_context_data(**kwargs)

        profile = self.request.user.financial_profile

        categories = Category.objects.filter(profile=profile)
        transactions = Transaction.objects.filter(profile=profile)

        spending_by_category = {}
        for category in categories:
            total = transactions.filter(category=category).aggregate(models.Sum("amount"))["amount__sum"] or 0
            spending_by_category[category.category_name] = total

        context["spending_by_category"] = spending_by_category

        return context

