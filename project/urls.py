# File: project/urls.py
# Author: Valentina Mora (vmora19@bu.edu), 11/23/2025
# Description: Url paths for project application

from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', DashboardView.as_view(), name="show_dashboard"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="show_profile"),
    path('show_all_transactions', TransactionListView.as_view(), name="show_all_transactions"),
    path('profile/create_note', CreateNoteView.as_view(), name="create_note"),
    path('profile/create_transaction', CreateTransactionView.as_view(), name="create_transaction"),
    path('show_all_notes', NotesListView.as_view(), name="show_all_notes"),
    path('transaction/<int:pk>/update', UpdateTransactionView.as_view(), name="update_transaction"),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name="show_transaction"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('create_category', CreateCategoryView.as_view(), name="create_category"),
    path('account/<int:pk>/', AccountDetailView.as_view(), name="show_account"),
    path('transaction/<int:pk>/delete', DeleteTransactionView.as_view(), name="delete_transaction"),
    path('note/<int:pk>/delete', NotesDeleteView.as_view(), name="delete_note"),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name="update_note"),
    path('note/<int:pk>/', NoteDetailView.as_view(), name="show_note"),
    path('login/', UserLoginView.as_view(), name="login"),
    path("logout/", custom_logout_view, name="logout"),
    path('dashboard/', DashboardView.as_view(), name="show_dashboard"),
    path('create_account', CreateAccountView.as_view(), name="create_account"),
]