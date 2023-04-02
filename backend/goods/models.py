from django.db import models
from django.urls import reverse
from catalog.models import Manufacturer, Aroma, Volume


class Candle(models.Model):
    title = models.CharField(max_length=50, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True, related_name='manufacturers_candle')
    summary = models.TextField(max_length=100, blank=True, help_text='Enter a description of the candle')
    aroma = models.ForeignKey(Aroma, on_delete=models.PROTECT, null=True, related_name='aromas_candle')
    volume = models.ManyToManyField(Volume, blank=True, related_name='volume_candles')
    link = models.CharField(max_length=50)
    image = models.ImageField(upload_to="candle/", blank=True, default="image-placeholder.png")
    
    def __str__(self):
        return self.title
        
    def display_volume(self):
        return ', '.join([f'{volume.weight} {volume.unit}' for volume in self.volume.all()])
    
    def volumes(self):
        return [f'{volume.weight} {volume.unit}' for volume in self.volume.all()]
    
    def get_good_url(self):
        return reverse('good', args=[self.title])
    
    def add_to_favorite(self):
        return reverse('favorite-add', args=[self.title])
    
    def del_to_favorite(self):
        return reverse('favorite-del', args=[self.title])
    

class Soap(models.Model):
    title = models.CharField(max_length=50, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True, related_name='manufacturers_soap')
    summary = models.TextField(max_length=100, blank=True, help_text='Enter a description of the soap')
    aroma = models.ForeignKey(Aroma, on_delete=models.PROTECT, null=True, related_name='aromas_soap')
    volume = models.ManyToManyField(Volume, blank=True, related_name='volume_soap')
    link = models.CharField(max_length=50)
    image = models.ImageField(upload_to="soap/", blank=True, default="image-placeholder.png")    
    
    def __str__(self):
        return self.title
        
    def display_volume(self):
        return ', '.join([f'{volume.weight} {volume.unit}' for volume in self.volume.all()])
    
    def volumes(self):
        return [f'{volume.weight} {volume.unit}' for volume in self.volume.all()]
    
    def get_good_url(self):
        return reverse('good', args=[self.title])
    
    def add_to_favorite(self):
        return reverse('favorite-add', args=[self.title])
    
    def del_to_favorite(self):
        return reverse('favorite-del', args=[self.title])
 
 
class Cream(models.Model):
    title = models.CharField(max_length=50, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True, related_name='manufacturers_cream')
    summary = models.TextField(max_length=100, blank=True, help_text='Enter a description of the soap')
    aroma = models.ForeignKey(Aroma, on_delete=models.PROTECT, null=True, related_name='aromas_cream')
    volume = models.ManyToManyField(Volume, blank=True, related_name='volume_cream')
    link = models.CharField(max_length=50)
    image = models.ImageField(upload_to="cream/", blank=True, default="image-placeholder.png")    
    
    def __str__(self):
        return self.title  
    
    def display_volume(self):
        return ', '.join([f'{volume.weight} {volume.unit}' for volume in self.volume.all()])
    
    def volumes(self):
        return [f'{volume.weight} {volume.unit}' for volume in self.volume.all()]
    
    def get_good_url(self):
        return reverse('good', args=[self.title])
    
    def add_to_favorite(self):
        return reverse('favorite-add', args=[self.title])
    
    def del_to_favorite(self):
        return reverse('favorite-del', args=[self.title])
