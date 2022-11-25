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


class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    phone_nr = PhoneNumberField(null=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class Booking(models.Model):

    booking_nr = models.AutoField(primary_key=True)
    guest = models.ForeignKey(
            Guest, on_delete=models.CASCADE, related_name='guest')
    cabin = models.CharField(max_length=6, choices=cabin_choice, null=False)
    nr_of_guests = ((1, '1 Guest'), (2, '2 Guests'), (3, '3 Guests'),
                    (4, '4 Guests'), (5, '5 Guests'), (6, '6 Guests'),
                    (7, '2 Guests'), (8, '2 Guests'), (9, '9 Guests'),
                    (10, '2 Guests'), (11, '2 Guests'), (12, '12 Guests'))
    guests = models.IntegerField(choices=nr_of_guests, default=2)
    arrival = models.DateField()
    departure = models.DateField()

    def __str__(self):
        return str(self.booking_id)