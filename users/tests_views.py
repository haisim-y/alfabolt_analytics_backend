from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser
from . import views
from . import serializers

# Create your tests here.

class UserApiTestCase(APITestCase):


    def setUp(self):
        # Create a user for testing
        self.username = "testuser"
        self.password = "testpassword"
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)

    def test_user_registration_post(self):
        url = reverse("register")
        data = {
            "username": "newuser7",
            "email": "newuser7@example.com",
            'first_name':'test',
            "password": "newpassword",
        }
        response = self.client.post(url, data, format="json")
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):

        valid_data = {
            "username": self.username,
            "password": self.password,
        }
        url = reverse("user-login")
        response = self.client.post(url, valid_data, format="json")
        print(response.status_code)
        # Assert the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("tokens",response.data)
        #self.assertIn("access_token",response.data)
    def test_unsuccessful_login(self):

        invalid_data = {

            "username": 'invalid',
            "password": 'invalid',
        }
        url = reverse("user-login")
        response = self.client.post(url, invalid_data, format="json")
        print(response.status_code)
        # Assert the status code
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

