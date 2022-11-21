from . import views
from django.urls import path


urlpatterns = [
    path('', views.cabinOland, name='cabin_oland'),
    path('', views.cabinSalen, name='cabin_salen'),
]
