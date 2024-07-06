from django.contrib import admin
from .models import Product, Discount, Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Cart)