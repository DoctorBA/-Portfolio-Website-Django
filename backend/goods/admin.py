from django.contrib import admin
from .models import Candle, Soap, Cream


@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'aroma', 'display_volume', 'link')
    
    
@admin.register(Soap)
class SoapAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'aroma', 'display_volume', 'link')
    
    
@admin.register(Cream)
class CreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'aroma', 'display_volume', 'link')        
