from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProjectResource

@receiver(post_save,sender=ProjectResource)
def send_email(sender,instance,created,**kwargs):
    if created:
        subject = 'Welcome to ALfabolt!!\n'
        message = f'Hello {instance.resource.first_name},\n\nYou have been added to {instance.project.title}!'
        from_email = 'haisimyasin@outlook.com'  # Set the sender's email address
        recipient_list = [instance.resource.email]
        print(subject,message,from_email,recipient_list)
