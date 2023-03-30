from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=20, blank=True)
    address = models.TextField(max_length=50, blank=True, help_text="Enter manufacturer's address")
    image = models.ImageField(upload_to="manufacturer/", blank=True, default="image-placeholder.png")
        
    def __str__(self):
        return self.name
    
    def get_manufacturer_url(self):
        return reverse('manufacturer', args=[self.name])
    
    def get_goods_url(self):
        return reverse('goods-manufacturer', args=[self.name])
    
    
class Aroma(models.Model):
    name = models.CharField(max_length=20, unique=True)
    summary = models.TextField(max_length=100, help_text='Enter a description of the aroma')
    image = models.ImageField(upload_to="aroma/", blank=True, default="image-placeholder.png")
        
    def __str__(self):
        return self.name
    
    def get_aroma_url(self):
        return reverse('aroma', args=[self.name])
    
    def get_goods_url(self):
        return reverse('goods-aroma', args=[self.name])
    

class Volume(models.Model):
    weight = models.IntegerField()
    unit = models.TextField(max_length=20, help_text='Enter a description of the unit')
        
    def __str__(self):
        return str(self.weight)
    
    def get_volume_url(self):
        return reverse('volume', args=[self.weight])            
