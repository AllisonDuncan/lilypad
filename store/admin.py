from django.contrib import admin
from .models import Product, Cart, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)