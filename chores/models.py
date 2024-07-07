from django.db import models

#There should be relationship between a user and many chores
#There should be a relationship between a user and their star bank

# Create your models here.
class Chore(models.Model):
    class ChoreStatus(models.TextChoices):
        NEW = "NE"
        AVAILABLE = "AV"
        CLAIMED = "CL"
        INPROGRESS = "IP"
        COMPLETE = "CO"
    status = models.CharField(
        max_length=2,
        choices=ChoreStatus.choices,
        default=ChoreStatus.NEW
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    why = models.CharField(max_length=255, null=True, blank=True)
    due_date = models.DateField("due date", null=True, blank=True)
    completed_date = models.DateField("completed date", null=True, blank=True)
    required = models.BooleanField(default=False)
    claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(
        "ChoreList",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # default to current time
    # created_date = models.DateTimeField("created date") [default: `now()`]
    stars = models.IntegerField()
    def __str__(self):
        return self.name

# todo functions
# claim a chore
# complete a chore
# unclaim a chore
#


class ChoreList(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
