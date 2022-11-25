from django import forms
from .models import Guest, Booking
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from datetime import datetime


class GuestInfo(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'phone_nr')


class BookingInfo(forms.ModelForm):
    arrival_date = forms.DateField(widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))
    departure_date = forms.DateField(widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta:
        model = Booking
        fields = ('guests', 'cabin',)
