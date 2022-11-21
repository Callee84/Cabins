from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostNews(SummernoteModelAdmin):

    list_display = ('author', 'title', 'created', 'updated')
    search_fields = ['author', 'title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
