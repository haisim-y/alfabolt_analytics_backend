from django.db import models
from datetime import datetime
from alfabolt_analytics.baseModels import BaseModel
# Create your models here.

"""
resources
            -----> projectresource
project

 resources

"""

class Resource(BaseModel,models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True)
    leaving_date=models.DateField(blank=True,null=True)
    gender=models.CharField(max_length=20,blank=True,null=True)
    currenly_working=models.BooleanField(default=True)
    maximum_weekly_hours=models.IntegerField(default=40)
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.ForeignKey('Designation', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
class Level(BaseModel,models.Model):
    name=models.CharField(max_length=50,default='1')
    def __str__(self):
        return self.name
class Designation(BaseModel,models.Model):
    name=models.CharField(max_length=100,default='-')
    def __str__(self):
        return self.name
class Status(BaseModel,models.Model):
    name=models.CharField(max_length=50,default='-')
    def __str__(self):
        return self.name        
    
class Project(BaseModel,models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=datetime.now())
    end_date= models.DateField(blank=True,null=True)
    currently_ongoing=models.BooleanField(default=True)
    domain=models.ForeignKey('Domain',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.title
class Domain(BaseModel,models.Model):
    name=models.CharField(max_length=100,default='Tech')
    def __str__(self):
        return self.name
class ProjectResource(BaseModel,models.Model):

    resource=models.ForeignKey(Resource, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    role=models.CharField(max_length=100)
    resource_joining_date = models.DateField(default=datetime.now)
    resource_ending_date=models.DateField(null=True,blank=True)
    resource_currently_working=models.FileField(default=True)
    project_lead = models.BooleanField(default=False)
    allocated_weekly_hour=models.IntegerField(default=40)

    def __str__(self):
        role_name=self.get_role_display()
        return f"{self.resource} in {self.project.title} as {role_name}"
    
class Technology(BaseModel,models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ResourceTechnology(BaseModel,models.Model):

    resource=models.ForeignKey(Resource, on_delete=models.CASCADE)
    technology=models.ForeignKey(Technology,on_delete=models.CASCADE)
    experience_in_years=models.IntegerField()

    def __str__(self):
        return f"{self.resource.first_name} {self.resource.last_name} has {self.experience_in_years} years experience in {self.technology.name}"
