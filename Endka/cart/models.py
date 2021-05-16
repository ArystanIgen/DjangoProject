from django.db import models
from auth_.models  import Profile
from service.models import *
from Endka import settings
from django.utils.translation import ugettext_lazy as _

class Cart(models.Model):
    customer=models.OneToOneField(Profile,related_name='carts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):

    cart = models.ForeignKey(Cart,related_name='cart_items',on_delete=models.CASCADE)
    item = models.ForeignKey(Item,related_name='items',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)