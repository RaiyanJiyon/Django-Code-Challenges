from django.shortcuts import render

# Create your views here.
def greet_user(request, username):
    context = {
        'username': username
    }
    return render(request, 'app/greet_user.html', context = context)
