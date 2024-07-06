from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    def __str__(self):
        return self.user_name
    #relationship to bank account
    #relationship to cart
    #relationship to chores
    

class Bank(models.Model):
    id = models.IntegerField()
    account_number = models.IntegerField()
    balance = models.IntegerField()
    transaction_history = models.OneToManyField("Transaction")
    def __str__(self):
        return self.account_number
    # add to balance
    # remove from balance
    # print balance
    # print transaction history

class Transaction(models.Model):
    request_time = models.DateTimeField()
    amount = models.IntegerField()
    request_type = "add or subtract"
    # account number