from django.shortcuts import render

# Create your views here.
def new_f(request):
    return render(request,'new.html')
