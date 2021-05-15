from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from .validators import *
from auth_.models import *


class Restaurant(models.Model):
    owner=models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="retaurants")
    res_name = models.CharField(max_length=100, blank=False)
    res_image = models.ImageField(blank=True,null=True, upload_to='res_images/',validators=[validate_size, validate_extension])
    res_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+879999999'. Up to 15 digits allowed.")
    res_phone_number = models.CharField(validators=[res_phone_regex], max_length=17, blank=True,null=True)
    res_description = models.TextField(default = 'none')
    city = models.CharField(_("city"), max_length=64, default="Almaty")
    country = models.CharField(_("country"), max_length=64, default="Kazakhstan")

    class Meta:
        verbose_name_plural = "Restraunt's Infos"


    def __str__(self):
        return self.res_name


class Item(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="items")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=False)
    item_image = models.ImageField(upload_to='item_images/',blank=True,null=True,validators=[validate_size, validate_extension])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.item_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name