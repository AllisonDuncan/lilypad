from django.contrib import admin
from .models import Bank, Transaction

# Register your models here.

admin.site.register(Bank)
admin.site.register(Transaction)