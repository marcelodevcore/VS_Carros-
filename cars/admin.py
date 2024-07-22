from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'plate', 'value')
    search_fields = ('model','brand', 'value')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)




