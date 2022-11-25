from django.shortcuts import render
from .forms import ContactForm
from django.views import View

# Create your views here.


class ContactUs(View):

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST)

        return render(request, 'contact.html', {'form': form})
