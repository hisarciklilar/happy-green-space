from django.contrib import admin
from .models import Post, Reply
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on')
    search_fields = ['body']
