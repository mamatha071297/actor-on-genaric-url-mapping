from django.urls import path
from app2.views import *

app_name='two'

urlpatterns=[
    path('first/',first,name='first'),
    path('new/',new,name='new'),
]