from . import views
from django.urls import path
from .views import PostGuestView, AddGuestPost, EditGuestPost, DeleteGuestPost


urlpatterns = [
    path('', views.PostGuestView.as_view(), name='guestbook'),
    path('add_post/', AddGuestPost.as_view(), name='add_guest_post'),
    path('guestbook/edit<int:pk>', views.EditGuestPost.as_view(),
         name='edit_guest_post'),
    path('guestbook/deleted/<int:pk>', views.DeleteGuestPost.as_view(),
         name='deleted_guest_post'),
]
