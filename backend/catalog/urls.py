from django.contrib import admin
from django.urls import path
from .views import IndexView
from django.conf import settings


urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
]