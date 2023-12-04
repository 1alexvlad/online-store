from django.urls import path
from myapp.views import *

app_name = "myapp"

urlpatterns = [
    # path('', index, name="index"),
    path('', ProductListView.as_view(), name="index"),
# name нужно чтобы каждый раз не вводить путь url (index.html)
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('additem/', add_item, name="add_item"),
    path('udpateitem/<int:my_id>/', update_item, name="update_item"),
    path('delete/<int:my_id>/', delete_item, name="delete_item"),
]