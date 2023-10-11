from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Resource
from . import views
from . import serializers

# Create your tests here.

class ResourceApiTestCase(APITestCase):
#------------------------------------------------------Resources View Test
    def test_post_resource(self):

        data={
            "first_name": "Kamlesh",
            "last_name": "Kumar",
            "email": "kkumar.bscs20seecs@seecs.edu.pk",
            "designation": "Data Analyst"
        }
        url=reverse('resource')
        response = self.client.post(url,data, format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_update_resource(self):

        Resource.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            designation="Software Engineer"
        )
        url=reverse('resource_update',args=[1])


        data={
            "last_name": "l",
        }
        response = self.client.patch(url,data, format='json')
        print(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_resourse_list(self):
        Resource.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            designation="Software Engineer"
        )
        url=reverse('resource')
        response=self.client.get(url)
        print(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_resource_detail(self):

        Resource.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            designation="Software Engineer"
        )
        url=reverse('resource_detail',args=[1])
        response=self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_delete_resource_detail(self):
        # Create a resource with a known ID (e.g., ID=1)
        Resource.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            designation="Software Engineer"
        )
        
        # Get the URL for the resource detail endpoint with ID=1
        url = reverse('resource_delete', args=[1])
        
        # Send a DELETE request to the resource detail endpoint
        response = self.client.delete(url)
        
        # Check whether the response status code is 204 No Content, which indicates successful deletion
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Optionally, you can also check if the resource with ID=1 no longer exists in the database
        # resource_exists = Resource.objects.filter(id=1).exists()
        # self.assertFalse(resource_exists, "Resource should not exist after deletion")
#-------------------------------------------------------------------------------------------------------------------------------------
    
