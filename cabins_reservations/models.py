from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


cabin_choice = (
        ('SAL', 'Sälen'),
        ('OLA', 'Öland'),
)

status_booking = (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('canceled', 'canceled')
)


nr_of_guests = ((1, '1 Guest'), (2, '2 Guests'), (3, '3 Guests'),
                (4, '4 Guests'), (5, '5 Guests'), (6, '6 Guests'),
                (7, '2 Guests'), (8, '2 Guests'), (9, '9 Guests'),
                (10, '2 Guests'), (11, '2 Guests'), (12, '12 Guests'),
                (13, '14 Guests'), (14, '14 Guests'),)


class Cabin(models.Model):
    cabin_id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    beds = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    phone_nr = PhoneNumberField(null=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class Booking(models.Model):

    booking_id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(
            Guest, on_delete=models.CASCADE, related_name='guest')
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    guests = models.IntegerField(choices=nr_of_guests, default=2)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    status = models.CharField(
            max_length=10, choices=status_booking, default="pending")

    def __str__(self):
        return str(self.booking_id)
