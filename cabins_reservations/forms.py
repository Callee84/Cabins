from django import forms
from .models import Guest, Booking
from phonenumber_field import PhoneNumberField


class GuestInfo(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'phone_nr')

