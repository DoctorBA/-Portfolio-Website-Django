from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from catalog.models import Manufacturer, Aroma
from .models import Candle, Soap, Cream


#<-- View goods -->  
class ManufacturerGoodsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request, name):
        manufacturer = Manufacturer.objects.get(name=name)
        goods_list = (
            Candle.objects.filter(manufacturer=manufacturer)
            .union(Soap.objects.filter(manufacturer=manufacturer))
            .union(Cream.objects.filter(manufacturer=manufacturer))
        )
        paginator = Paginator(goods_list, 9)
        page_number = request.GET.get('catalog-page')
        goods = paginator.get_page(page_number) 
        params = {'goods': goods}
        
        return render(request, self.template_name, params)   
    
 
class AromaGoodsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request, name):
        aroma = Aroma.objects.get(name=name)
        goods_list = (
            Candle.objects.filter(aroma=aroma)
            .union(Soap.objects.filter(aroma=aroma))
            .union(Cream.objects.filter(aroma=aroma))
        )
        paginator = Paginator(goods_list, 9)
        page_number = request.GET.get('catalog-page')
        goods = paginator.get_page(page_number) 
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
        
    
#<-- Favorite View -->     
class FavoriteAddView(TemplateView):
    
    @method_decorator(login_required)
    def get(self, request, title):
        good = (
            Candle.objects.filter(title=title)
            .union(Soap.objects.filter(title=title))
            .union(Cream.objects.filter(title=title))
        )
        favorite = request.user
        favorite.products.add(good)
        
        return redirect('catalog-index')