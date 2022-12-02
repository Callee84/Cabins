from . import views
from django.urls import path
from .views import contact


urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('contact/contact_sent', views.contact_sent, name="sent")
]
