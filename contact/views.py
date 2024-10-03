from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            contact_form = ContactForm()
            messages.add_message(request, messages.SUCCESS, "Message received! I endeavour to respond within 2 working days.")
            # Process the form data
            # For example, send an email or save to the database
            
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
