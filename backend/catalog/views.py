from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Manufacturer, Aroma
from goods.models import Candle, Soap, Cream


#<-- Catalog View -->  
class IndexView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods = Candle.objects.all().union(Soap.objects.all()).union(Cream.objects.all())
        numb = goods.count()
        catalog = {str(k*3):v for k, v in enumerate(goods, 1)}
        
        params = {'goods': goods, 'numb': numb, 'catalog':catalog }

        return render(request, self.template_name, params)
    
    
class ManufacturersView(TemplateView):
    template_name = 'catalog/manufacturer.html'
    
    def get(self, request):
        manufacturers = Manufacturer.objects.all()
        
        params = {'manufacturers': manufacturers}

        return render(request, self.template_name, params)


class AromasView(TemplateView):
    template_name = 'catalog/aroma.html'
    
    def get(self, request):
        aromas = Aroma.objects.all()
        
        params = {'aromas': aromas}

        return render(request, self.template_name, params)


class CandlesView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods = Candle.objects.all()
        candles = "candles"
        params = {'goods': goods, 'candles': candles}
        
        return render(request, self.template_name, params)


class SoapsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods = Soap.objects.all()
        soaps = "soaps"
        params = {'goods': goods, 'soaps': soaps}
        
        return render(request, self.template_name, params)
 
 
class CreamsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods = Cream.objects.all()
        creams = "creams"
        params = {'goods': goods, 'creams': creams}
        
        return render(request, self.template_name, params)
            
    
#<-- Navigation View -->     
class NavigView(TemplateView):
    ...
   
       
    
    