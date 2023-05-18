from django.contrib import admin
from django.utils.html import format_html

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar_thumbnail', 'name', 'company_name', 'contact_number', 'notes')

    def avatar_thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.avatar.url))

    avatar_thumbnail.short_description = 'avatar'

    list_per_page = 10


admin.site.register(Customer, CustomerAdmin)
