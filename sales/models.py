from django.db import models
from alfabolt_analytics.baseModels import BaseModel

# Create your models here.

class Outreach(BaseModel,models.Model):
    RESPONSE_STATUS=[
        ('Positive','Positive Response'),
        ('Negative', 'Negative Response'),
        ('No_Response','No Response'),
    ]
    OUTREACH_METHOD=[
        ('Phone ','Phone Number'),
        ('Email','Email Address')

    ]
    contact_name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=100,blank=True,null=True)
    contact_phone=models.CharField(max_length=20,blank=True,null=True)
    outreach_date = models.DateField(auto_now_add=True)
    outreach_method = models.CharField(max_length=50,choices=OUTREACH_METHOD)
    outreach_message = models.TextField(blank=True,null=True)
    response_status = models.CharField(max_length=50, choices=RESPONSE_STATUS ,blank=True, null=True)
    scheduled_call = models.BooleanField(default=False)

    def __str__(self):
        return f"Outreach to {self.contact_name} on {self.outreach_date}"
    
    # @classmethod
    # def success_rate(cls):
    #     successRate=0
    #     total_outreach=cls.objects.count()
    #     positive_outreach=cls.objects.filter(response_status='Positive').count()
    #     if positive_outreach>0:
    #         successRate=(positive_outreach/total_outreach)*100
    #     else:
    #         successRate=0
    #     return successRate


