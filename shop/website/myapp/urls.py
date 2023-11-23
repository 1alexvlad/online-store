from django.urls import path
from myapp.views import *

urlpatterns = [
    path('hello/', index),
    path('contacts/', contact),
]