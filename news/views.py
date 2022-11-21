from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class showNews(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('created')
    template_name = 'news.html'
    paginate_by = 5


# def news(request):
#     return render(request, 'news.html')
