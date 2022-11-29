from django import forms
from .models import Guest, Booking
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from datetime import datetime
from .models import cabin_choice, nr_of_guests


class Booking(forms.Form):
    guest = forms.CharField(max_length=200)
    guests = forms.ChoiceField(choices=nr_of_guests)
    cabin = forms.ChoiceField(choices=cabin_choice)
    arrival_date = forms.DateField(widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))
    departure_date = forms.DateField(widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))
