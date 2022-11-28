from django.contrib import admin
from .models import PostGuest, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PostGuest)
class PostGuestNews(SummernoteModelAdmin):

    list_display = ('author', 'title', 'created', 'updated')
    search_fields = ['author', 'title']
    summernote_fields = ('content',)


admin.site.register(Category)
