from django.urls import path
from rcd.views import *

app_name='bng'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('Abd/',Abd,name='Abd'),
    
]