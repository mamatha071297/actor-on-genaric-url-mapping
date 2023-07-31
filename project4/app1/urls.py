from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns = [
    path('new_f/',new_f,name='new_f')
] 