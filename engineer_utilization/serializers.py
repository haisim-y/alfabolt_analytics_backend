from rest_framework import serializers
from .models import Project,ProjectResource,Resource,ResourceTechnology,Technology

                                        #Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id',"title","description","start_date","budget_in_dollars"]
                                        #Resource Serializer
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resource
        fields=['id','first_name','last_name','email','designation']

#------------------------------------------------------------Project Resource Serializer-----------------------------
class ResourceProjectGetSerializer(serializers.ModelSerializer):
    resource=ResourceSerializer()
    project=ProjectSerializer()
    class Meta:
        model=ProjectResource
        depth=1
        fields=['project','role','resource_joined_date','project_lead']
class ResourceProjectHideResourceSerializer(serializers.ModelSerializer):
    #resource=ResourceSerializer()
    project =ProjectSerializer()
    class Meta:
        model=ProjectResource
        depth=1
        fields=['project','role','resource_joined_date','project_lead']

class ResourceProjectHideProjectSerializer(serializers.ModelSerializer):
    resource=ResourceSerializer()
    #project=ProjectSerializer()
    class Meta:
        model=ProjectResource
        depth=1
        fields=['resource','role','resource_joined_date','project_lead']

class ResourceProjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectResource
 
        fields='__all__'

                #-----------------------Technology Serializer---------------------------------------------------------------------------
class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model=Technology
        fields=['id','name','domain']
#------------------------------------ResourceTechnology Serializer----------------------------------------------------------------------
class ResourceTechnologyGetSerializer(serializers.ModelSerializer):
    resource=ResourceSerializer()
    technology=TechnologySerializer()
    class Meta:
        model=ResourceTechnology
        depth=1
        fields=['resource','technology','experience_in_years']
class ResourceTechnologyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResourceTechnology
        fields=fields=['resource','technology','experience_in_years']

class ResourceTechnologyHideTechnologySerializer(serializers.ModelSerializer):
    resource=ResourceSerializer()
    #technology=TechnologySerializer()
    class Meta:
        model=ResourceTechnology
        depth=1
        fields=['resource','experience_in_years']
class ResourceTechnologyHideResourceSerializer(serializers.ModelSerializer):
    #resource=ResourceSerializer()
    technology=TechnologySerializer()
    class Meta:
        model=ResourceTechnology
        depth=1
        fields=['technology','experience_in_years']
#-----------------------------------------------------------------------------------------------------------------------------------------


