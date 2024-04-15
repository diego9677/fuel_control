from django.contrib import admin

from .models import FuelType, Fueling


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'description')
    list_display_links = ('pk', 'name')
    search_fields = ('name', 'description')


@admin.register(Fueling)
class FuelingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fuel_type', 'liters')
    search_fields = ('total', 'liters')
    list_display_links = ('pk', 'fuel_type')
