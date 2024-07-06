from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Chore

# Create your views here.
def index(request):
    latest_chore_list = Chore.objects.order_by("due_date")
    template = loader.get_template("chores/index.html")
    context = {
        "latest_chore_list": latest_chore_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, chore_id):
    return HttpResponse("You're looking at chore %s." % chore_id)

def results(request, chore_id):
    response = "You're looking at the results of chore %s."
    return HttpResponse(response % chore_id)
