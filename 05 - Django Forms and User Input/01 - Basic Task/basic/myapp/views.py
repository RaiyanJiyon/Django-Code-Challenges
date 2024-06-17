from django.shortcuts import render
from .forms import Registration

def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            student_id = form.cleaned_data['student_id']
            course_name = form.cleaned_data['course_name']
            course_section = form.cleaned_data['course_section']
            email = form.cleaned_data['email']

            # Correctly passing a dictionary as context
            return render(request, 'myapp/success.html', {'name': name})
    else:
        form = Registration()

    return render(request, 'myapp/registration.html', {'form': form})
