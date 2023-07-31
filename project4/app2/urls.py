from django.urls import path
from app2.views import *

app_name='something'

urlpatterns = [
    path('new/',new,name='new'),
] 