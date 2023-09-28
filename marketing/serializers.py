from rest_framework import serializers
from .models import Leads,Post

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

