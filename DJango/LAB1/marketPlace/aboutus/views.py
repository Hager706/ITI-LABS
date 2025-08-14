from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>About Us Page</h1>")