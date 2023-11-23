from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World sfask')

def contact(request):
    return HttpResponse('<h1>Это наши контакты</h1>')