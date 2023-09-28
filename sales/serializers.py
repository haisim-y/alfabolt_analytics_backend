from rest_framework import serializers
from .models import Outreach

class OutreachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outreach
        fields='__all__'