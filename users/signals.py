from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save,sender=CustomUser)
def register(sender,instance,created,**kwargs):
    if created:
        log=print(f'{instance.username} is registered !!!!')

        print(log)
