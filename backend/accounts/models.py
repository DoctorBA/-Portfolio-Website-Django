from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from goods.models import Candle, Soap, Cream


class User(AbstractUser, PermissionsMixin):

    username = None
    email = models.EmailField(_('email'), unique=True)
    favorite_сandle = models.ManyToManyField(Candle, blank=True)
    favorite_soap = models.ManyToManyField(Soap, blank=True)
    favorite_cream = models.ManyToManyField(Cream, blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
        
    def __str__(self):
        return self.email  
    
    def get_favorite_list(self):
        return [good for good in (self.favorite_cream.all()
                                                .union(self.favorite_soap.all())
                                                .union(self.favorite_сandle.all()))]
    
    def get_total_favorite(self):
        return len([good for good in (self.favorite_cream.all()
                                                  .union(self.favorite_soap.all())
                                                  .union(self.favorite_сandle.all()))])
    
    def display_favorite(self):
        return " ".join([good.title for good in (self.favorite_cream.all()
                                                  .union(self.favorite_soap.all())
                                                  .union(self.favorite_сandle.all()))])