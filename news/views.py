from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.


class showNews(ListView):
    # view for news
    model = Post
    queryset = Post.objects.order_by('created')
    template_name = 'news.html'
    paginate_by = 6
    ordering = ['-created']


class DetailNews(DetailView):
    # views for news details
    model = Post
    template_name = 'news_detail.html'


class AddPost(CreateView):
    # view for adding news
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class EditPost(UpdateView):
    # view for editing news
    model = Post
    template_name = 'edit_post.html'
    fields = '__all__'


class DeletePost(DeleteView):
    # view for deleting news
    model = Post
    success_url = reverse_lazy('news')
    template_name = 'deleted_post.html'
