from django.urls import path
from csk.views import *

app_name='chennai'

urlpatterns=[
    path('msd/',msd,name='msd'),
    path('reina/',reina,name='reina'),
    path('jadeja/',jadeja,name='jadeja'),

]