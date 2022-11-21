from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.showNews.as_view(), name='news'),
    path('summernote/', include('django_summernote.urls')),
]
