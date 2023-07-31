from django.urls import path
from app1.views import *

app_name='one'

urlpatterns=[
    path('first/',first,name='first'),
    path('new/',new,name='new'),
]