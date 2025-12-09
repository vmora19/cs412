from django.contrib import admin

# Register your models here.
from .models import Profile, Category, Note, Account, Transaction
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Account)
admin.site.register(Transaction)