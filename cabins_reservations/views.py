from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.models import User
import datetime
from .models import Guest, Booking
from .forms import GuestInfo, BookingInfo


# Create your views here.


def cabinOland(request):
    return render(request, 'cabin_oland.html')


def cabinSalen(request):
    return render(request, 'cabin_salen.html')

def avalibility(request, User):
    pass
