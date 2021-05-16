from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_.models import *
from cart.models import CartItem
from orders.models import *


@receiver(post_save, sender=OrderItem)
def order_created(sender, instance, created, **kwargs):
    if created:
        CartItem.objects.filter(cart=instance.carts).delete()

