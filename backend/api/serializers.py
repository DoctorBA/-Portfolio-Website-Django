from rest_framework import serializers
from goods.models import Candle, Soap, Cream
from catalog.models import Manufacturer, Aroma


class CandleSerializer(serializers.ModelSerializer):
    manufacturer = serializers.ReadOnlyField(source='manufacturer.country')
    aroma = serializers.ReadOnlyField(source='aroma.name')
    volume = serializers.ReadOnlyField(source='volume.weight')
    
    class Meta:
        model = Candle
        fields = ['id', 'title', 'manufacturer', 'summary', 'aroma', str('volume'), 'link', 'image']
        
  
class SoapSerializer(serializers.ModelSerializer):
    manufacturer = serializers.ReadOnlyField(source='manufacturer.country')
    aroma = serializers.ReadOnlyField(source='aroma.name')
    volume = serializers.ReadOnlyField(source='volume.weight')
    
    class Meta:
        model = Soap
        fields = ['id', 'title', 'manufacturer', 'summary', 'aroma', 'volume', 'link', 'image']
        
      
class CreamSerializer(serializers.ModelSerializer):
    manufacturer = serializers.ReadOnlyField(source='manufacturer.country')
    aroma = serializers.ReadOnlyField(source='aroma.name')
    volume = serializers.ReadOnlyField(source='volume.weight')
    
    class Meta:
        model = Cream
        fields = ['id', 'title', 'manufacturer', 'summary', 'aroma', 'volume', 'link', 'image']  
        

class ManufacturerSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'address', 'image']   
        
        
class AromaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aroma
        fields = ['id', 'name', 'summary', 'image']                         