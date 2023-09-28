from rest_framework import serializers
from .models import Project,ProjectResource,Resource,ResourceTechnology,Technology

                                        #Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'
                                        #Resource Serializer
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resource
        fields=['first_name','last_name','designation']

                                        #Project Resource Serializer
class ResourceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectResource
        fields='__all__'

                                        #Technology Serializer
class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model=Technology
        fields=['name']

                                        #ResourceTechnology Serializer
class ResourceTechnologySerializer(serializers.ModelSerializer):
    resource=ResourceSerializer()
    technology=TechnologySerializer()
    class Meta:
        model=ResourceTechnology
        depth=1
        fields='__all__'



