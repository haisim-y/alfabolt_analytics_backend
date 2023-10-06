from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Project,ProjectResource,Resource,ResourceTechnology,Technology
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ResourceTechnologyPostSerializer,ResourceProjectPostSerializer,ProjectSerializer,ResourceProjectPostSerializer,ResourceProjectGetSerializer,ResourceProjectHideProjectSerializer,ResourceProjectHideResourceSerializer,ResourceSerializer,ResourceTechnologyGetSerializer,TechnologySerializer,ResourceTechnologyHideTechnologySerializer,ResourceTechnologyHideResourceSerializer



# Create your views here.

""" 
                                PROJECT                                     

"""
class ProjectListCreateApiView(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    # def perform_create(self, serializer):
    #     title=serializer.validated_data.get('title')
    #     description=serializer.validated_data.get('description')
    #     if description is None:
    #         description=title
    #         serializer.save(title=title,description=description)

class ProjectDetailApiView(generics.RetrieveAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

class ProjectUpdateApiView(generics.UpdateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    lookup_field='pk'

class ProjectDeleteApiView(generics.DestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer


""" 
                                RESOURCE                                   

"""

class ResourceListCreateApiView(generics.ListCreateAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer


class ResourceDetailApiView(generics.RetrieveAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer

class ResourceUpdateApiView(generics.UpdateAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer
    lookup_field='pk'

class ResourceDeleteApiView(generics.DestroyAPIView):
    queryset=Resource.objects.all()
    serializer_class=ProjectSerializer



""" 
                                TECHNOLOGY                               

"""

class TechnologyListCreateApiView(generics.ListCreateAPIView):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializer

class TechnologyDetailApiView(generics.RetrieveAPIView):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializer

class TechnologyUpdateApiView(generics.UpdateAPIView):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializer
    lookup_field='pk'

class TechnologyDeleteApiView(generics.DestroyAPIView):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializer

""" 
                                RESOURCE TECHNOLOGY                               

"""

class GetTechnologyResourceListApiView(generics.ListAPIView):

    #queryset=ProjectResource.objects.all()
    serializer_class=ResourceTechnologyHideTechnologySerializer
    #pagination_class=CustomPagination
    def get_queryset(self):
        tech_id=self.kwargs['id']
        return ResourceTechnology.objects.filter(technology=tech_id)

class GetResourceTechnologyListApiView(generics.ListAPIView):

    #queryset=ProjectResource.objects.all()
    serializer_class=ResourceTechnologyHideResourceSerializer
    #pagination_class=CustomPagination
    def get_queryset(self):
        resource_id=self.kwargs['id']
        return ResourceTechnology.objects.filter(resource=resource_id)

class ResourceTechDetailApiView(generics.RetrieveAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologyGetSerializer

class ResourceTechUpdateApiView(generics.UpdateAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologyPostSerializer
    lookup_field='pk'

class ResourceTechDeleteApiView(generics.DestroyAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologyPostSerializer
class ResourceTechCreateApiView(generics.CreateAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologyPostSerializer

""" 
    ---------------------------------------------- PROJECT RESOURCE-----------------------------------------------------------------------                     

# """
# class CustomPagination(PageNumberPagination):
#     page_size = 2  # Set the number of items per page
#     page_size_query_param = 'page_size'  # Allow clients to specify the page size via a query parameter
    


class GetResourceProjectListApiView(generics.ListAPIView):
    #queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectHideResourceSerializer
    def get_queryset(self):
        resource_id=self.kwargs['id']
        return ProjectResource.objects.filter(resource=resource_id)
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()

    #     Calculate the total number of projects for the resource
    #     total_projects = queryset.count()

    #     serializer = self.get_serializer(queryset, many=True)
    #     data = serializer.data

    #     Create a custom response dictionary that includes the count and project data
    #     response_data = {
    #         'total_projects of resource': total_projects,
    #         'projects': data,
    #     }

    #     return Response(response_data)
class GetProjectResourceListApiView(generics.ListAPIView):

    #queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectHideProjectSerializer
    #pagination_class=CustomPagination
    def get_queryset(self):
        project_id=self.kwargs['id']
        return ProjectResource.objects.filter(project=project_id)
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     paginator=self.pagination_class()
    #     page=paginator.paginate_queryset(queryset,request)

    #     # Calculate the total number of resources in the project
    #     total_resources = queryset.count()

    #     serializer = self.get_serializer(queryset, many=True)
    #     data = serializer.data

    #     # Create a custom response dictionary that includes the count and project data
    #     response_data = {
    #         'total_resources in this project': total_resources,
    #         'resources info': data,
    #     }

    #     return paginator.get_paginated_response(data)
     
    

class ProjectResourceDetailApiView(generics.RetrieveAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectGetSerializer


#post resource project
class ProjectResourceCreateApiView(generics.CreateAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectPostSerializer
class ProjectResourceUpdateApiView(generics.UpdateAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectPostSerializer
    lookup_field='pk'

class ProjectResourceDeleteApiView(generics.DestroyAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectPostSerializer
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------