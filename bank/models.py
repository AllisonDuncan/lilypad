from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Bank(models.Model):
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=50, default="My Bank Account")
    balance = models.IntegerField()
    # transaction_history = models.OneToManyField("Transaction")
    def __str__(self):
        return self.account_name
    # add to balance
    # remove from balance
    # print balance
    # print transaction history

class RequestType(models.TextChoices):
    ADD = "ADD"
    SUBTRACT = "SUB"

class TransactionStatus(models.TextChoices):
    PROCESSING = "P"
    COMPLETE = "C"

class Transaction(models.Model):
    request_time = models.DateTimeField()
    amount = models.IntegerField()
    request_type = models.CharField(max_length=3, choices=RequestType.choices, default=RequestType.ADD)
    status = models.CharField(max_length=1, choices=TransactionStatus.choices, default=TransactionStatus.PROCESSING)
    account_number = models.IntegerField()
