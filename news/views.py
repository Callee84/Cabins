from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class showNews(ListView):
    model = Post
    queryset = Post.objects.order_by('created')
    template_name = 'news.html'
    paginate_by = 5


class DetailNews (DetailView):
    model = Post
    template_name = 'news_detail.html'
