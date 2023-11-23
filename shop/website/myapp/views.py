from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "myapp/index.html", context)

# Динамическая ссылка
def indexItem(request, id):
    return HttpResponse("Your item id is: " + str(id))

def contact(request):
    return render(request, "myapp/contacts.html")