from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    # model for category
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('guestbook')


class PostGuest(models.Model):
    # model for review in guestbook
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=750)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, default='no_category')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('guestbook')
