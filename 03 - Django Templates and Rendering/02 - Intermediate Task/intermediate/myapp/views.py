from django.shortcuts import render
from .models import Product

# Create your views here.
def display(request):
    data = Product.objects.all()
    context = {
        'data': data,
        'extra_info': 'This is extra information'
    }

    return render(request, 'myapp/display.html', context=context)