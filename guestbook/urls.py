from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostGuestView.as_view(), name='guestbook')
]
