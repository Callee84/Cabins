# Generated by Django 3.2.16 on 2022-11-26 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0003_auto_20221122_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='postguest',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=225, unique=True),
            preserve_default=False,
        ),
    ]
