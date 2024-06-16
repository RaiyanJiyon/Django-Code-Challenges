from django.urls import path
from .views import book_list

urlpatterns = [
    path('books/<int:publisher_id>', book_list, name='book_list')
]
