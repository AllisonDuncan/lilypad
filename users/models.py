from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    bank = models.IntegerField(blank=True, null=True)
    cart = models.IntegerField(blank=True, null=True)
    chores = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.user_name
    
