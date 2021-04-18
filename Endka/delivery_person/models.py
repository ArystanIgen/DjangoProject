from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class DeliveryPerson(models.Model):
    dp_name = models.CharField(max_length=64)
    dp_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+879999999'. Up to 15 digits allowed.")
    dp_phone_number = models.CharField(validators=[dp_phone_regex], max_length=17, blank=True)