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
        fields=['id','first_name','last_name','email','designation','resource_status','maximum_weekly_hours','level']

#------------------------------------------------------------Project Resource Serializer-----------------------------
class ResourceProjectGetSerializer(serializers.ModelSerializer):
    resource=ResourceSerializer()
    project=ProjectSerializer()
    class Meta:
        model=ProjectResource
        depth=1
        fields=['resource','project','role','resource_joined_date','project_lead','allocated_weekly_hour']
class ResourceProjectHideResourceSerializer(serializers.ModelSerializer):
    #resource=ResourceSerializer()
    project =ProjectSerializer()
    class Meta:
        model=ProjectResource
        depth=1
        fields=['project','role','resource_joined_date','project_lead','allocated_weekly_hour']

class ResourceProjectHideProjectSerializer(serializers.ModelSerializer):
    resource=ResourceSerializer()
    #project=ProjectSerializer()
    class Meta:
        model=ProjectResource
        depth=1
        fields=['resource','role','resource_joined_date','project_lead','allocated_weekly_hour']

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

# class ProjectResourceSerializer(serializers.ModelSerializer):
#     overall_utilization_in_percentage = serializers.SerializerMethodField()
#     class Meta:
#         model=ProjectResource
#         fields='__all__'
#     def get_overall_utilization_in_percentage(self,obj):
#         #retrieving all ProjectResourceInstance for a resource
#         filter_resource=ProjectResource.objects.filter(resource=obj.resource)
#         max_weekly_hour_resource=obj.resource.maximum_weekly_hours
#         allocated_weekly_hours_resource_all_projects=sum(pr.allocated_weekly_hour for pr in filter_resource)
#         if max_weekly_hour_resource>0:
#             return ((allocated_weekly_hours_resource_all_projects/max_weekly_hour_resource)*100)
#         else :
#             return 0
        
class ResourceProjectDashboardSerializer(serializers.ModelSerializer):
    project_list=serializers.SerializerMethodField()
    technology_list=serializers.SerializerMethodField()
    overall_utilization_percent=serializers.SerializerMethodField()

    
    class Meta:
        model = Resource
        fields = [ 'id','first_name', 'last_name', 'resource_status', 'maximum_weekly_hours', 'level', 'project_list','technology_list','overall_utilization_percent']
    
    def get_project_list(self,obj):
        project_resources=ProjectResource.objects.filter(resource=obj)
        projects=[pr.project.title for pr in project_resources]
        #project_title=[project.title for project in projects]
        return projects
    def get_overall_utilization_percent(self,obj):
        max_weekly_hour_resource=obj.maximum_weekly_hours
        project_resources=ProjectResource.objects.filter(resource=obj)
        sum_allocated_hours=sum(pr.allocated_weekly_hour for pr in project_resources)
        return ((sum_allocated_hours/max_weekly_hour_resource)*100)
    def get_technology_list(self,obj):
        tech_resources=ResourceTechnology.objects.filter(resource=obj)
        tech_names=[rt.technology.name for rt in tech_resources]
        return tech_names





