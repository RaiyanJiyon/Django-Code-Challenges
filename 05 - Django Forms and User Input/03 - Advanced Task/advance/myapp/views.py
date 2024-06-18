from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Form submitted successfully!')
            return redirect('success')
        else:
            messages.error(request, 'Please correct the errors below.')
            
    else:
        form = StudentForm()

    return render(request, 'myapp/student_form.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html')
