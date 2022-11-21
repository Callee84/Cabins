from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.news, name='news'),
    path('summernote/', include('django_summernote.urls')),
]
