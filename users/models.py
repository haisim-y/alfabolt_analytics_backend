from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.'

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
   
    
    
    def __str__(self):
        return self.username


