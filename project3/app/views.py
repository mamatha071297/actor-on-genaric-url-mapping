from django.shortcuts import render
from django.http import HttpResponse

def sample(request):
    return HttpResponse('<marquee><h1 style=color:red;>hello i am mamatha</h1></marquee>')

# Create your views here.
