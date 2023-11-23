from django.urls import path
from myapp.views import *

urlpatterns = [
    path('hello/', index),
    path('hello/<int:my_id>/', indexItem),

    path('contacts/', contact),
]