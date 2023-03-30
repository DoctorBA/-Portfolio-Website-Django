from rest_framework.views import APIView
from rest_framework import generics
from . import serializers
from goods.models import Candle, Soap, Cream
from catalog.models import Manufacturer, Aroma



class CandleList(generics.ListAPIView):
    queryset = Candle.objects.all()
    serializer_class = serializers.CandleSerializer


class SoapList(generics.ListAPIView):
    queryset = Soap.objects.all()
    serializer_class = serializers.SoapSerializer
    
    
class CreamList(generics.ListAPIView):
    queryset = Cream.objects.all()
    serializer_class = serializers.CreamSerializer        


class ManufacturerList(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
    
    
class AromaList(generics.ListAPIView):
    queryset = Aroma.objects.all()
    serializer_class = serializers.AromaSerializer    
    
    
#<-- Detail View -->         
class CandleDetall(generics.RetrieveAPIView):
    queryset = Candle.objects.all()
    serializer_class = serializers.CandleSerializer   
    
    
class SoapDetall(generics.RetrieveAPIView):
    queryset = Soap.objects.all()
    serializer_class = serializers.SoapSerializer      
    
    
class CreamDetall(generics.RetrieveAPIView):
    queryset = Cream.objects.all()
    serializer_class = serializers.CreamSerializer    
    
    
class ManufacturerDetall(generics.RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer   
    
 
class AromaDetall(generics.RetrieveAPIView):
    queryset = Aroma.objects.all()
    serializer_class = serializers.AromaSerializer           