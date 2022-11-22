from django.shortcuts import render
from django.views.generic import ListView
from .models import PostGuest
# Create your views here.

# def guestbook(request):
#     return render(request, 'guestbook.html')


class PostGuestView(ListView):
    model = PostGuest
    template_name = 'guestbook.html'
    paginate_by = 10
