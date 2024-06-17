from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def features(request):
    return render(request, 'myapp/features.html')

def pricing(request):
    return render(request, 'myapp/pricing.html')
