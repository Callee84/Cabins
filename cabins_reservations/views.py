from django.shortcuts import render, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from .models import Guest, Booking, Cabin, cabin_choice
from .forms import Booking
from .availability import check_availability
from django.urls import reverse_lazy
import datetime


class CabinOland(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'cabin_oland.html')


class CabinSalen(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'cabin_salen.html')


class GuestView(ListView):
    model = Guest


class CabinView(ListView):
    model = Cabin


def new_booking(self, request, User=User, *args, **kwargs):
    booking_form = Booking(data=request.POST)

    if booking_form.is_valid():
        guest_name = request.POST.get('guest')
        guest_no_of_guests = request.POST.get('guests')
        guest_arrival_date = request.POST.get('arrival_date')
        guest_departure_date = request.POST.get('departure_date')

        # convert to date format
        conv_guest_arrival = datetime.datetime.strptime(
            guest_arrival_date, '%d/%m/%Y')
        conv_guest_dep = datetime.datetime.strptime(
            guest_departure_date, '%d/%m/%Y')

        booking = booking_form.save(commit=False)
            # Pass formatted date & customer in to model
        booking.arrival_date = conv_guest_arrival
        booking.departure_date = conv_guest_departure
        reservation.customer = customer
            # Save reservation
        booking_form.save()
