from django.shortcuts import render
from rest_framework import permissions,generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .serializers import UserLoginSerializers,UserRegistrationSerializers,UserUpdateSerializers
from .models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .permissions import IsAdminOrSelf
from rest_framework.views import APIView
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
            refresh_token=RefreshToken.for_user(user)
            res={
                 'refresh_token':str(refresh_token),
                 'access_token': str(refresh_token.access_token)
            }
            #token,created=Token.objects.get_or_create(user=user)



            return Response({'token': res, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogin(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserLoginSerializers

    def create(self,request,*args,**kwargs):
        #         getting username and password from body
        username=request.data.get('username')
        password=request.data.get('password')
       # print('password before authenticcation ', password)

        #user=get_object_or_404(self.queryset,username=username)
        user=authenticate(username=username,password=password)
        #print('password after authenticcation ', user.password)

        if user is None:
            return Response("Invalid username or password", status=status.HTTP_404_NOT_FOUND)
        refresh_token=RefreshToken.for_user(user)
        access_token = refresh_token.access_token
        res={
             'refresh_token':str(refresh_token),
             'access_token':str(access_token),
        }
       # token,created=Token.objects.get_or_create(user=user)

        serializer=self.get_serializer(user)
        #print('after login ', user.password)
        return Response({'tokens':res, 'user': serializer.data})

class TokenRefreshView(APIView):
     def post (self , request ):
          refresh_token=request.data.get('refresh_token')
          if not refresh_token:
               return Response("Refresh token is required",status=status.HTTP_404_NOT_FOUND)
          try:
               
            token=RefreshToken(refresh_token)
            access_token=token.access_token
          except:
               return Response("Invalid Refresh Token",status=status.HTTP_404_NOT_FOUND)
          data={'access_token' :  str(access_token)}
          return Response({'Token':data},status=status.HTTP_200_OK )


    
class UserDestroyView(generics.DestroyAPIView):
        queryset=CustomUser.objects.all()
        serializer_class=UserRegistrationSerializers
        permission_classes=[IsAdminOrSelf]


class UserDetailView(generics.RetrieveAPIView):
        permission_classes=[IsAuthenticated]
        queryset=CustomUser.objects.all()
        serializer_class=UserRegistrationSerializers
        lookup_field='pk'

class UserUpdateView(generics.UpdateAPIView):
        permission_classes=[IsAdminOrSelf]
        queryset=CustomUser.objects.all()
        serializer_class=UserUpdateSerializers
        lookup_field='pk'
     
        







