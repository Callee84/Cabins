from . import views
from django.urls import path, include
from .views import showNews, DetailNews


urlpatterns = [
    path('', views.showNews.as_view(), name='news'),
    path('news/<slug:slug>', views.DetailNews.as_view(), name='news_details'),
    path('summernote/', include('django_summernote.urls')),
]
