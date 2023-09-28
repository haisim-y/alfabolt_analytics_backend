from django.db import models
from alfabolt_analytics.baseModels import BaseModel
# Create your models here.

"""
resources
            -----> projectresource
project

 resources

"""

class Resource(BaseModel,models.Model):
    GENDER=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other')
    ]
    SKILL=[
        ('Management','Project Management'),
        ('ML','Machine Learning'),
        ('Dvelopment','Software Devlopment'),
        ('Hr','Human Resource')
    ]
    DESIGNATION=[
        ('Software Engineer','Software Engineer'),
        ('Data Scientist','Data Scientist'),
        ('Data Analyst','Data Analyst'),
        ('HR','Human Resource'),
        ('CEO','Cheif Executive Officer'),
        ('CTO','Cheif Technology Officer'),
        ('Designer','Designer')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True,choices=SKILL)
    availability = models.BooleanField(default=True)
    hire_date = models.DateField(auto_now_add=True)
    gender=models.CharField(max_length=8,choices=GENDER)
    designation=models.CharField(max_length=100,choices=DESIGNATION)

    def __str__(self):
        return self.first_name
class Project(BaseModel,models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
   # end_date= models.DateField()
    budget_in_dollars = models.DecimalField(max_digits=10, decimal_places=2)
    #team_member=models.ManyToManyField(Resource,through="ProjectResource")
    def __str__(self):
        return self.title
class ProjectResource(BaseModel,models.Model):
    ROLES=[

        ('Frontend ','Frontend Developer'),
        ('Backend','Backend Developer'),
        ('Devops','Devops Developer'),
        ('Cloud','CLoud Architect'),
        ('Data Science','Data Scientist')
    ]
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    role=models.CharField(max_length=100,choices=ROLES)
    resource_joined_date = models.DateField()
    project_lead = models.BooleanField(default=False)
    def __str__(self):
        role_name=self.get_role_display()
        return f"{self.resource} in {self.project.title} as {role_name}"
    
class Technology(BaseModel,models.Model):
    TECH_DOMAINS=[
        ('Backend Development','Backend Development'),
        ('Frontend Development','Frontend Development'),
        ('Data Science','Data Science'),
        ('Sales','Sales'),
    ]
    name = models.CharField(max_length=100)
    domain=models.CharField(max_length=50,choices=TECH_DOMAINS)

    def __str__(self):
        return self.name

class ResourceTechnology(BaseModel,models.Model):

    resource=models.ForeignKey(Resource, on_delete=models.CASCADE)
    technology=models.ForeignKey(Technology,on_delete=models.CASCADE)
    experience_in_years=models.IntegerField()

    def __str__(self):
        return f"{self.resource.first_name} {self.resource.last_name} has {self.experience_in_years} years experience in {self.technology.name}"





