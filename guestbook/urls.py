from . import views
from django.urls import path
from .views import PostGuestView, AddGuestPost


urlpatterns = [
    path('', views.PostGuestView.as_view(), name='guestbook'),
    path('add_post/', AddGuestPost.as_view(), name='add_guest_post'),
]
