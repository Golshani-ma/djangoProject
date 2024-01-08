from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['pk','title', 'author', 'image', 'counted_views', 'status', 'published_date', 'created_date']
    list_filter = ['status', 'author']
    search_fields = ['title', 'counted_views', 'status', 'published_date', 'created_date']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
