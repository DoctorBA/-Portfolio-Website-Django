from django.urls import path, include
from .views import ManufacturerGoodsView, ManufacturerView, AromaGoodsView, \
AromaView, GoodView, FavoriteAddView, FavoritelAllView, FavoriteDelView
   

urlpatterns = [
   path('manufacturer-<str:name>/', ManufacturerGoodsView.as_view(), name='goods-manufacturer'),
   path('manufacturer/<str:name>/', ManufacturerView.as_view(), name='manufacturer'),
   path('aroma-<str:name>/', AromaGoodsView.as_view(), name='goods-aroma'),
   path('aroma/<str:name>/', AromaView.as_view(), name='aroma'),
   path('del_all/', FavoritelAllView.as_view(), name='favorite-del_all'),
   path('add/<str:title>/', FavoriteAddView.as_view(), name='favorite-add'),
   path('del/<str:title>/', FavoriteDelView.as_view(), name='favorite-del'),   
   path('<str:title>/', GoodView.as_view(), name='good'),   
] 