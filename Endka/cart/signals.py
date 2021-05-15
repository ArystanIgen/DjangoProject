from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_.models import *
from .models import Cart


@receiver(post_save, sender=Profile)
def cart_created(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(customer=instance)