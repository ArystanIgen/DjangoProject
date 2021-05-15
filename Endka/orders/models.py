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




    def __str__(self):
        return self.id

