from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data here
            name = form.cleaned_data.get('name')
            student_id = form.cleaned_data.get('student_id')
            gender = form.cleaned_data.get('gender')
            birth_date = form.cleaned_data.get('birth_date')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            phone_number = form.cleaned_data.get('phone_number')

            # Assuming you would save data to the database or perform other logic here

            # Use Django messages framework to show a success message
            messages.success(request, 'Form submitted successfully!')

            # Redirect to a new URL or render a success template
            return redirect('success')
    else:
        form = StudentForm()

    return render(request, 'myapp/student_form.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html')
