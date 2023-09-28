from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Leads,Post
from .serializers import PostSerializer,LeadSerializer


class PostListCreateApiView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer


class PostDetailApiView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostUpdateApiView(generics.UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='pk'

class PostDeleteApiView(generics.DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer


#Leads


class LeadListCreateApiView(generics.ListCreateAPIView):
    queryset=Leads.objects.all()
    serializer_class=LeadSerializer


class LeadDetailApiView(generics.RetrieveAPIView):
    queryset=Leads.objects.all()
    serializer_class=LeadSerializer

class LeadUpdateApiView(generics.UpdateAPIView):
    queryset=Leads.objects.all()
    serializer_class=LeadSerializer
    lookup_field='pk'

class LeadDeleteApiView(generics.DestroyAPIView):
    queryset=Leads.objects.all()
    serializer_class=LeadSerializer