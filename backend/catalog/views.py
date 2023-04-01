from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from .models import Manufacturer, Aroma
from goods.models import Candle, Soap, Cream


#<-- Catalog View -->  
class IndexView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods_list = Candle.objects.all().union(Soap.objects.all()).union(Cream.objects.all())
        paginator = Paginator(goods_list, 9)
        page_number = request.GET.get('catalog-page')
        goods = paginator.get_page(page_number)        
        params = {'goods': goods }

        return render(request, self.template_name, params)
    
    
class ManufacturersView(TemplateView):
    template_name = 'catalog/manufacturer.html'
    
    def get(self, request):
        goods_list = Manufacturer.objects.all()
        paginator = Paginator(goods_list, 3)
        page_number = request.GET.get('manufacturers-page')
        manufacturers = paginator.get_page(page_number)
        params = {'manufacturers': manufacturers}

        return render(request, self.template_name, params)


class AromasView(TemplateView):
    template_name = 'catalog/aroma.html'
    
    def get(self, request):
        goods_list = Aroma.objects.all()
        paginator = Paginator(goods_list, 3)
        page_number = request.GET.get('aromas-page')
        aromas = paginator.get_page(page_number)
        params = {'aromas': aromas}

        return render(request, self.template_name, params)


class CandlesView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods_list = Candle.objects.all()
        paginator = Paginator(goods_list, 9)
        page_number = request.GET.get('catalog-page')
        goods = paginator.get_page(page_number)   
        candles = "candles"
        params = {'goods': goods, 'candles': candles}
        
        return render(request, self.template_name, params)


class SoapsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods_list = Soap.objects.all()
        paginator = Paginator(goods_list, 9)
        page_number = request.GET.get('catalog-page')
        goods = paginator.get_page(page_number)  
        soaps = "soaps"
        params = {'goods': goods, 'soaps': soaps}
        
        return render(request, self.template_name, params)
 
 
class CreamsView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        goods_list = Cream.objects.all()
        paginator = Paginator(goods_list, 9)
        page_number = request.GET.get('catalog-page')
        goods = paginator.get_page(page_number) 
        creams = "creams"
        params = {'goods': goods, 'creams': creams}
        
        return render(request, self.template_name, params)
    
  
#<-- Catalog search -->     
class SearchView(TemplateView):
    template_name = 'main.html'
    
    def post(self, request):
        content = request.POST['content']
        
        goods_list = (
            Candle.objects.filter(title__icontains=content)
            .union(Soap.objects.filter(title__icontains=content))
            .union(Cream.objects.filter(title__icontains=content))
        )
        paginator = Paginator(goods_list, 9)
        page_number = request.GET.get('catalog-page')
        goods = paginator.get_page(page_number) 
        params = {'goods': goods}
        
        return render(request, self.template_name, params)       
    
    