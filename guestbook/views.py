from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import PostGuest
from .forms import AddGuestPost
# Create your views here.

# def guestbook(request):
#     return render(request, 'guestbook.html')


class PostGuestView(ListView):
    model = PostGuest
    queryset = PostGuest.objects.order_by('created')
    template_name = 'guestbook.html'
    paginate_by = 10
    ordering = ['-created']


class AddGuestPost(CreateView):
    model = PostGuest
    form_class = AddGuestPost
    template_name = 'add_guest_post.html'
    # fields = '__all__'


class EditGuestPost(UpdateView):
    model = PostGuest
    template_name = 'edit_guest_post.html'
    fields = '__all__'


class DeleteGuestPost(DeleteView):
    model = PostGuest
    success_url = reverse_lazy('guestbook')
    template_name = 'deleted_post.html'
