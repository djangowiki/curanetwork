from django.contrib import admin
from .models import Property, Booking


# Register the Property and Bookings in the Django Admin
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'long', 'lat']


admin.site.register(Booking)