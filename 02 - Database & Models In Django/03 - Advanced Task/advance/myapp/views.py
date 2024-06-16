from django.shortcuts import render, get_object_or_404
from .models import Publisher, Book

# Create your views here.
def book_list(request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id)
    books = Book.objects.filter(publisher=publisher)
    return render(request, 'myapp/book_list.html', {'books':books, 'publisher':publisher})

