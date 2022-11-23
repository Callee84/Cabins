from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length=225, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('news')
