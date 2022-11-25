from . import views
from django.urls import path


urlpatterns = [
    path('oland', views.cabinOland.as_view(), name='cabin_oland'),
    path('salen', views.cabinSalen, name='cabin_salen'),
]
