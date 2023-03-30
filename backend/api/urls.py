from django.urls import path, include
from .views import CandleList, SoapList, CreamList, ManufacturerList, AromaList, \
CandleDetall, SoapDetall, CreamDetall, ManufacturerDetall, AromaDetall


urlpatterns = [
    path('candles/', CandleList.as_view(), name='api-candles'),
    path('candles/<int:pk>/', CandleDetall.as_view(), name="api-candle"),
    path('soaps/', SoapList.as_view(), name='api-soaps'),
    path('soaps/<int:pk>/', SoapDetall.as_view(), name="api-soap"),
    path('creams/', CreamList.as_view(), name='api-creams'),
    path('creams/<int:pk>/', CreamDetall.as_view(), name="api-cream"),
    path('manufacturers/', ManufacturerList.as_view(), name='api-manufacturers'),
    path('manufacturers/<int:pk>/', ManufacturerDetall.as_view(), name='api-manufacturer'),
    path('aromas/', AromaList.as_view(), name='api-aromas'),
    path('aromas/<int:pk>/', AromaDetall.as_view(), name='api-aroma'),
] 