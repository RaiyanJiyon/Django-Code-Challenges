from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from .forms import ContactForm

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to session
            request.session['contact_name'] = form.cleaned_data['name']
            request.session['contact_email'] = form.cleaned_data['email']
            request.session['contact_message'] = form.cleaned_data['message']
            
            # Save to database (if needed)
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            contact.save()
            
            return redirect('success')
        return render(request, 'contact.html', {'form': form})
