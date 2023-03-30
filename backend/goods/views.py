from django.shortcuts import render
from django.views.generic import TemplateView
from catalog.models import Manufacturer, Aroma
from .models import Candle, Soap, Cream


#<-- View goods -->  
class ManufacturerGoodsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request, name):
        manufacturer = Manufacturer.objects.get(name=name)
        goods = (
            Candle.objects.filter(manufacturer=manufacturer)
            .union(Soap.objects.filter(manufacturer=manufacturer))
            .union(Cream.objects.filter(manufacturer=manufacturer))
        )
        params = {'goods': goods}
        
        return render(request, self.template_name, params)   
    
 
class AromaGoodsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request, name):
        aroma = Aroma.objects.get(name=name)
        goods = (
            Candle.objects.filter(aroma=aroma)
            .union(Soap.objects.filter(aroma=aroma))
            .union(Cream.objects.filter(aroma=aroma))
        )
        params = {'goods': goods}
        
        return render(request, self.template_name, params)
    
    
#<-- Detail View -->                    
class GoodView(TemplateView):
    template_name = 'catalog/good.html'
    
    def get(self, request, title):
        good = (
            Candle.objects.filter(title=title)
            .union(Soap.objects.filter(title=title))
            .union(Cream.objects.filter(title=title))
        )
        params = {'good': good[0]}
        
        return render(request, self.template_name, params)    
    

class ManufacturerView(TemplateView):
    template_name = 'catalog/manufacturer.html'
    
    def get(self, request, name):
        manufacturers = Manufacturer.objects.get(name=name)
        params = {'manufacturers': [manufacturers]}
        
        return render(request, self.template_name, params)
    
    
class AromaView(TemplateView):
    template_name = 'catalog/aroma.html'
    
    def get(self, request, name):
        aromas = Aroma.objects.get(name=name)
        params = {'aromas': [aromas]}
        
        return render(request, self.template_name, params)    