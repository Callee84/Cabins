# Generated by Django 3.2.16 on 2022-11-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabins_reservations', '0006_auto_20221128_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(choices=[(1, '1 Guest'), (2, '2 Guests'), (3, '3 Guests'), (4, '4 Guests'), (5, '5 Guests'), (6, '6 Guests'), (7, '7 Guests'), (8, '8 Guests'), (9, '9 Guests'), (10, '10 Guests'), (11, '11 Guests'), (12, '12 Guests'), (13, '14 Guests'), (14, '14 Guests')], default=2),
        ),
    ]