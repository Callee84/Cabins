from datetime import datetime
from .models import Cabin, Booking


def check_availability(cabin, arrival_date, departure_date):
    avail_list = []
    booking_list = Booking.objects.filter(cabin=cabin)
    for booking in booking_list:
        if booking.arrival_date > departure_date.date or booking.departure_date < arrival_date:
            avail_list.append(True)

    return all(avail_list)