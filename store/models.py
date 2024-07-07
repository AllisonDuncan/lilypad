from django.db import models
# from users import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    display_price = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=50, blank=True, null=True)
    available_for_sale = models.BooleanField(default=False)
    cart = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
    
    #inventory or number of items in stock

class Cart(models.Model):
    name = models.CharField(max_length=50, default="My Cart")
    # products = models.ManyToManyField("Product")
    def __str__(self):
        return self.name
    # user = models.OneToOneField(users.User)


class Order(models.Model):
    order_id = models.IntegerField()
    products_in_order = models.ManyToManyField("Product")
    total = models.IntegerField()
    user = models.IntegerField()
    # created = models.DateField("created time") [default: `now()`]
    