from django.urls import path
from .views import IndexView, CandlesView, SoapsView, CreamsView, \
ManufacturersView, AromasView, SearchView, FavoriteView


urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('catalog/candles/', CandlesView.as_view(), name='catalog-candles'),
    path('catalog/soaps/', SoapsView.as_view(), name='catalog-soaps'),
    path('catalog/creams/', CreamsView.as_view(), name='catalog-creams'),    
    path('catalog/manufacturers/', ManufacturersView.as_view(), name='catalog-manufacturers'),    
    path('catalog/aromas/', AromasView.as_view(), name='catalog-aromas'),
    path('catalog/favorite/', FavoriteView.as_view(), name='catalog-favorite'),
    path('catalog/search/', SearchView.as_view(), name='catalog-search'),    
]