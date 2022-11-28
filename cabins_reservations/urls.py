from . import views
from django.urls import path


urlpatterns = [
    path('oland', views.CabinOland.as_view(), name='cabin_oland'),
    path('salen', views.CabinSalen.as_view(), name='cabin_salen'),
    path('booking', views.BookingView.as_view(), name='booking'),
    path('', views.BookingView.as_view(), name='home'),
]
