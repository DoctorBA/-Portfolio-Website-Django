from django.urls import path, include
from .views import ManufacturerGoodsView, ManufacturerView, AromaGoodsView, \
AromaView, GoodView, FavoriteAddView
   

urlpatterns = [
   path('manufacturer-<str:name>/', ManufacturerGoodsView.as_view(), name='goods-manufacturer'),
   path('manufacturer/<str:name>/', ManufacturerView.as_view(), name='manufacturer'),
   path('aroma-<str:name>/', AromaGoodsView.as_view(), name='goods-aroma'),
   path('aroma/<str:name>/', AromaView.as_view(), name='aroma'),
   path('add/<str:title>/', FavoriteAddView.as_view(), name='favorite-add'),
   path('<str:title>/', GoodView.as_view(), name='good'),
   
] 