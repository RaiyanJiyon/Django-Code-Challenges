from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')

def contact(request):
    return render(request, 'myapp/contact.html')