from django.shortcuts import render, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import FormView
import datetime
from .models import Guest, Booking, Cabin
from .forms import Availibility
from .availibility import check_availability


class CabinOland(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'cabin_oland.html')

    # return render(request, 'cabin_oland.html')


class CabinSalen(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'cabin_salen.html')


class BookingView(FormView):
    form_class = Availibility
    template_name = 'booking.html'

    def valid_form(self, form):
        data = form.cleaned_data
        cabin_list = Cabin.objects.filter(category=data['cabin_choice'])
        avalible_dates = []
        for cabin in cabin_list:
            if check_availability(
                    cabin, data['arrival_date'], data['departure_date']):
                avalible_dates.append(cabin)

        if len(avalible_dates) > 0:
            cabin = avalible_dates[0]
            booking = Booking.objects.create(
                user=self.request.user,
                cabin=cabin,
                arrival_date=data['arrival_date'],
                departure_date=data['departure_date'],
            )
            booking.save()
            return HttpResponse(booking)
            success_url = reverse_lazy('home')

        else:
            return HttpResponse(
                'This date is unavalible for this date, please choose anohter date.')
