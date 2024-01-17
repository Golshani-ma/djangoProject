from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category
from blog.models import Comment


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['pk', 'title', 'author', 'image', 'counted_views', 'status', 'published_date', 'created_date']
    list_filter = ['status', 'author']
    search_fields = ['title', 'counted_views', 'status', 'published_date', 'created_date']
    summernote_fields = ('content',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = '-empty-'
    list_display = ['name', 'post', 'approved', 'create_date']
    list_filter = ['name', 'post', 'approved']
    search_fields = ['post', 'name', 'create_date']
    summernote_fields = ('content',)


admin.site.register(Comment, CommentAdmin)
