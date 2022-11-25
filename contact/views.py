from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = {'form': ContactForm()}
    return render(request, 'contact.html', contact_form)
