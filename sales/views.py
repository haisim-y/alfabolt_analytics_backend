from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Outreach
from .serializers import OutreachSerializer

# Create your views here.

class OutreachListCreateApiView(generics.ListCreateAPIView):
    queryset=Outreach.objects.all()
    serializer_class=OutreachSerializer


class OutreachDetailApiView(generics.RetrieveAPIView):
    queryset=Outreach.objects.all()
    serializer_class=OutreachSerializer

class OutreachUpdateApiView(generics.UpdateAPIView):
    queryset=Outreach.objects.all()
    serializer_class=OutreachSerializer
    lookup_field='pk'

class OutreachDeleteApiView(generics.DestroyAPIView):
    queryset=Outreach.objects.all()
    serializer_class=OutreachSerializer

