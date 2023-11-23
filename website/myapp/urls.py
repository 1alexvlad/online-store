from django.urls import path
from myapp.views import *

app_name = "myapp"

urlpatterns = [
    path('hello/', index),
# name нужно чтобы каждый раз не вводить путь url (index.html)
    path('hello/<int:my_id>/', indexItem, name="detail"),

    path('contacts/', contact),
]