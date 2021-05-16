from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from auth_.models import *



@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = UserNew.objects.get(id=instance.user.id)
    user.delete()

@receiver(post_save, sender=UserNew)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)