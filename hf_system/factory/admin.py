from django.contrib import admin
from django.utils.html import format_html

from factory.models import ModelInfo
from django.db import models
from django.forms import widgets
from django.utils.html import format_html


class ModelBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "show_image", "name", "goods_shelf", "row", "col", "create_time", "update_time"]
    list_display_links = ('id', 'name')
    search_fields = ('name__icontains',)

    formfield_overrides = {
        models.ImageField: {'widget': widgets.ClearableFileInput(attrs={'accept': 'image/*'})},
    }

    def show_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.model_image.url))

    show_image.short_description = 'Image'

    list_per_page = 10

admin.site.register(ModelInfo, ModelBaseAdmin)
