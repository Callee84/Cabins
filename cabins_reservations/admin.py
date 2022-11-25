from django.contrib import admin
from .models import Guest, Booking


@admin.register(Guest)
class GuestAdminInfo(admin.ModelAdmin):

    list_display = ('guest_id', 'first_name', 'last_name', 'email', 'phone_nr')


@admin.register(Booking)
class GuestBookingInfo(admin.ModelAdmin):
    list_display = ('booking_id', 'guest', 'cabin', 'guests', 'status',
                    'arrival_date', 'departure_date')
