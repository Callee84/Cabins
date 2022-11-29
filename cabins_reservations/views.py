from django.shortcuts import render, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from .models import Guest, Booking, Cabin, cabin_choice
from .forms import Booking
from .availability import check_availability
from django.urls import reverse_lazy


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


class BookingView(FormView):
    form_class = Booking
    template_name = 'booking.html'
    success_url = reverse_lazy('booking')

    def form_valid(self, form):
        data = form.cleaned_data
        cabin_list = Cabin.objects.filter(name=data['cabin'])
        avalible_cabin = []
        for cabin in cabin_list:
            if check_availability(
                   cabin, data.date['arrival_date'], data.date['departure_date']):
                avalible_cabin.append(cabin)
            print(type(data['arrival_date']))
            booking.save()
 
        else:
            return HttpResponse(
               'Sorry, that date is already booked. Please pick another date.')
