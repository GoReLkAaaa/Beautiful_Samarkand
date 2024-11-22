from django.shortcuts import render
from django.db.models import Value
from django.db.models.functions import Greatest
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    templates = 'mainapp/index.html'
    return render(request, templates)

