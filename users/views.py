from django.shortcuts import render
from rest_framework import permissions,generics
from .serializers import UserLoginSerializers,UserRegistrationSerializers
from .models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


class UserRegistration(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserRegistrationSerializers
    permission_classes=[permissions.AllowAny]
#               overriding post request
    def create(self, request, *args, **kwargs):
                #getting serialized data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            #create a new instance of the model
            self.perform_create(serializer)
            #initializing user instance
            user=serializer.instance
            user.set_password(request.data['password'])
            user.save()
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogin(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserLoginSerializers

    def create(self,request,*args,**kwargs):
        #         getting username and password from body
        username=request.data.get('username')
        password=request.data.get('password')

        user=get_object_or_404(self.queryset,username=username)

        if not user.check_password(password):
            return Response("Invalid username or password", status=status.HTTP_404_NOT_FOUND)
        token,created=Token.objects.get_or_create(user=user)
        serializer=self.get_serializer(user)
        return Response({'token': token.key, 'user': serializer.data})


