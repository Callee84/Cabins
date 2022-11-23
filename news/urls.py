from . import views
from django.urls import path, include
from .views import showNews, DetailNews, AddPost, EditPost, DeletePost


urlpatterns = [
    path('', views.showNews.as_view(), name='news'),
    path('news/<slug:slug>', views.DetailNews.as_view(), name='news_details'),
    path('add_post', views.AddPost.as_view(), name='add_post'),
    path('news/edit/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('news/deleted', views.DeletePost.as_view(), name='deleted_post'),
    path('summernote/', include('django_summernote.urls')),
]
