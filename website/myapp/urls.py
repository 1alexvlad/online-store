from django.urls import path
from myapp.views import *

app_name = "myapp"

urlpatterns = [
    path('', index),
# name нужно чтобы каждый раз не вводить путь url (index.html)
    path('<int:my_id>/', indexItem, name="detail"),
]