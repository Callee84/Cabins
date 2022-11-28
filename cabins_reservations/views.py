from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
import datetime
from .models import Guest, Booking, Cabin
from .forms import GuestInfo, BookingInfo



# Create your views here.


class cabinOland(View):
    def get(self, request, *args, **kwargs):

        guest_info = GuestInfo()
        booking_info = BookingInfo()

        return render(request, 'cabin_oland.html', {
            'guest_info': guest_info,
            'booking_info': booking_info
        })

    # return render(request, 'cabin_oland.html')


class cabinSalen(View):
      def get(self, request, *args, **kwargs):

        guest_info = GuestInfo()
        booking_info = BookingInfo()

        return render(request, 'cabin_salen.html', {
            'guest_info': guest_info,
            'booking_info': booking_info
        })


def avalibility(request, User):

    avalible_date = len(Booking.objects.filter(
        arrival_date=arrival,
    ))


# def BookingEnquiry(View):
    