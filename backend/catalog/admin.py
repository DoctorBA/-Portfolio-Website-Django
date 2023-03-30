from django.contrib import admin
from .models import Manufacturer, Aroma, Volume


@admin.register(Manufacturer)
class Manufacturer(admin.ModelAdmin):
    list_display = ('name', 'country', 'address')
    
@admin.register(Aroma)
class Aroma(admin.ModelAdmin):
    list_display = ('name', 'summary')    


@admin.register(Volume)
class Volume(admin.ModelAdmin):
    list_display = ('weight', 'unit')   

