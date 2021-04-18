from django.db import models
from auth_.models import Profile
from service.models import Item

class Order(models.Model):
    profile=models.ForeignKey(Profile,related_name='profile_order',on_delete=models.CASCADE)
    item=models.ForeignKey(Item,related_name='item_order',on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=5, decimal_places=2)
    count=models.PositiveIntegerField(default=1)