from django.db import models
from auth_.models import Profile
from service.models import Item
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    adress=models.CharField(max_length=250,default="Saina")
    city = models.CharField(_("city"), max_length=64, default="Almaty")
    country = models.CharField(_("country"), max_length=64, default="Kazakhstan")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='profile_order',on_delete=models.CASCADE)
    item=models.ForeignKey(Item,related_name='item_order',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    owner=models.ForeignKey(Profile,related_name='profile_order',on_delete=models.CASCADE)

    def get_cost(self):
        return self.price * self.quantity
