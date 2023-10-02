from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','email','first_name','last_name','username','password']



class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','username','password']