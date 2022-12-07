from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import PostGuest
from .forms import AddGuestPost
# Create your views here.


class PostGuestView(ListView):
    # view for guestbook (reviews on site)
    model = PostGuest
    queryset = PostGuest.objects.order_by('created')
    template_name = 'guestbook.html'
    paginate_by = 9
    ordering = ['-created']


class ManageGuestPost(DetailView):
    # view when managing post
    model = PostGuest
    template_name = 'manage_guest_post.html'


class AddGuestPost(CreateView):
    # view for adding post
    model = PostGuest
    form_class = AddGuestPost
    template_name = 'add_guest_post.html'


class EditGuestPost(UpdateView):
    # view for editing guestbook
    model = PostGuest
    template_name = 'edit_guest_post.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.object.author
        return context


class DeleteGuestPost(DeleteView):
    # view for deleting post
    model = PostGuest
    success_url = reverse_lazy('guestbook')
    template_name = 'deleted_post.html'
