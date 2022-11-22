from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = '__all__'

