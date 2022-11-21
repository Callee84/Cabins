from . import views
from django.urls import path


urlpatterns = [
    path('oland', views.cabinOland, name='cabin_oland'),
    path('salen', views.cabinSalen, name='cabin_salen'),
]
