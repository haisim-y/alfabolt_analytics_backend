from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Project,ProjectResource,Resource,ResourceTechnology,Technology
from .serializers import ProjectSerializer,ResourceProjectSerializer,ResourceSerializer,ResourceTechnologySerializer,TechnologySerializer



# Create your views here.

""" 
                                PROJECT                                     

"""
class ProjectListCreateApiView(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        description=serializer.validated_data.get('description')
        if description is None:
            description=title
            serializer.save(title=title,description=description)

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

class ResourceTechListCreateApiView(generics.ListCreateAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologySerializer

class ResourceTechDetailApiView(generics.RetrieveAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologySerializer

class ResourceTechUpdateApiView(generics.UpdateAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologySerializer
    lookup_field='pk'

class ResourceTechDeleteApiView(generics.DestroyAPIView):
    queryset=ResourceTechnology.objects.all()
    serializer_class=ResourceTechnologySerializer

""" 
                                PROJECT RESOURCE                              

"""

class ProjectResourceListCreateApiView(generics.ListCreateAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectSerializer

class ProjectResourceDetailApiView(generics.RetrieveAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectSerializer

class ProjectResourceUpdateApiView(generics.UpdateAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectSerializer
    lookup_field='pk'

class ProjectResourceDeleteApiView(generics.DestroyAPIView):
    queryset=ProjectResource.objects.all()
    serializer_class=ResourceProjectSerializer
