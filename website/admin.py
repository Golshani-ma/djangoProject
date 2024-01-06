from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    list_filter = ['name', 'email']
    search_fields = ['name', 'message']




# Register your models here.
admin.site.register(Contact,ContactAdmin)
