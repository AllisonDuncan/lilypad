from django.db import models

#There should be relationship between a user and many chores
#There should be a relationship between a user and their star bank

# Create your models here.
class Chore(models.Model):
    class ChoreStatus(models.TextChoices):
        NEW = "NE", _("New")
        AVAILABLE = "AV", _("Available")
        CLAIMED = "CL", _("Claimed")
        INPROGRESS = "IP", _("In Progress")
        COMPLETE = "CO", _("Complete")
    id = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    why = models.CharField(max_length=255, null=True, blank=True)
    due_date = models.DateField("due date", null=True, blank=True)
    completed_date = models.DateField("completed date", null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=ChoreStatus
        default=ChoreStatus.NEW
    )
    required = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(
        ChoreList,
        on_delete=models.SET_NULL,
        null=True
    )
    # default to current time
    created_date = models.DateTimeField("created date") [default: `now()`]
    stars = models.IntegerField()
    def __str__(self):
        return self.name
    # if chore is required, due date is equal to today and vice versa
    # 
    # todo - claim chore function
    # complete chore function
    #


class ChoreList(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=50)

# null=true for fields that can be null in the db
# blank=True for fields that form validation should not run