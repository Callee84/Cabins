from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import PostGuest
# Create your views here.

# def guestbook(request):
#     return render(request, 'guestbook.html')


class PostGuestView(ListView):
    model = PostGuest
    template_name = 'guestbook.html'
    paginate_by = 10


class AddGuestPost(CreateView):
    model = PostGuest
    template_name = 'add_guest_post.html'
    fields = '__all__'
