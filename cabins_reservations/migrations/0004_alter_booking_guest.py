# Generated by Django 3.2.16 on 2022-11-28 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabins_reservations', '0003_auto_20221128_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabins_reservations.guest'),
        ),
    ]
