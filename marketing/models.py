from django.db import models
from alfabolt_analytics.baseModels import BaseModel
from datetime import datetime


class Post(BaseModel,models.Model):
    #id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    content = models.TextField()
    post_source = models.CharField(max_length=100)
    post_url = models.URLField(blank=True, null=True)
    likes_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
   

    def __str__(self):
        return f"Post ({self.id}) - {self.description}"
    
class Leads(BaseModel,models.Model):

    LEAD_STATUS_CHOICES = [
        ('new', 'New Lead'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('lost', 'Lost'),
        ('converted', 'Converted'),
     ]
    SECTOR_CHOICES= [
        ('Tech', 'Technology'),
        ('Finance', 'Financial Sector'),
        ('Health', 'Healthcare'),
    
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=True,null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)

    sector = models.CharField(max_length=100,choices=SECTOR_CHOICES, blank=True, null=True)
    lead_status = models.CharField(max_length=50,choices=LEAD_STATUS_CHOICES, blank=True, null=True) 
    
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True)
    response_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"