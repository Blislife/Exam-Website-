from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse

# Create your views here.

def index(response, id):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "select.html", {})

def logout_view(request):
    logout(request)