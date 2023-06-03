from django.contrib import admin

from staff.models import StaffBase


@admin.register(StaffBase)
class StaffBaseAdmin(admin.ModelAdmin):
    list_display = ['avatar', 'staff_code', 'phone_number', 'notes']
    list_display_links = ('staff_code',)
    search_fields = ('staff_code__icontains', 'phone_number__icontains')

    list_per_page = 10
