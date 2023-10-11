from django.test import TestCase
from .serializers import (
    ResourceProjectGetSerializer,
    ResourceProjectHideResourceSerializer,
    ResourceProjectHideProjectSerializer,
    ResourceProjectPostSerializer,
    ResourceSerializer,
    TechnologySerializer,
    ProjectSerializer
)
from .models import ProjectResource, Resource, Project

class ResourceSerializerTestCase(TestCase):
    def test_valid_data(self):
        valid_data = {
            'first_name':'haisim',
            'last_name':'yasin',
            'email':'haisim@gmail.com',
            'designation':'Software Engineer'
        }
        serializer=ResourceSerializer(data=valid_data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors,{})
    def test_missing_required_field(self):
        missing_name = {
            'last_name':'yasin',
            'email':'haisim@gmail.com',
            'designation':'Software Engineer'
        }
        serializer = ResourceSerializer(data=missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn('first_name', serializer.errors) 

    def test_invalid_data(self):
        invalid_data = {
            'first_name':'haisim',
            'last_name':'yasin',
            'email':1,
            'designation':'Software Engineer'
        }
        serializer=ResourceSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_output_data(self):
            output_data = {
            'first_name':'haisim',
            'last_name':'yasin',
            'email':'haisim@gmail.com',
            'designation':'Software Engineer'
        }
            serializer=ResourceSerializer(data=output_data)
            self.assertTrue(serializer.is_valid())
            serialized_data=serializer.data
            self.assertEqual(serialized_data,
                             {
            'first_name':'haisim',
            'last_name':'yasin',
            'email':'haisim@gmail.com',
            'designation':'Software Engineer'
        }
                             )

class TechnologySerializerTestCase(TestCase):


    def test_valid_data(self):
        valid_data = {
            'name': 'Django',
            'domain':'Backend Development'
        }
        serializer=TechnologySerializer(data=valid_data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors,{})
    def test_missing_required_field(self):
        missing_name = {
            'domain':'Backend Development'
        }
        serializer = TechnologySerializer(data=missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors) 

    def test_invalid_data(self):
        invalid_data = {
            'name': 'Django',
            'domain':123
        }
        serializer=TechnologySerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('domain', serializer.errors)

    def test_output_data(self):
            output_data = {
            'name': 'Django',
            'domain':'Backend Development'
        }
            serializer=TechnologySerializer(data=output_data)
            self.assertTrue(serializer.is_valid())
            serialized_data=serializer.data
            self.assertEqual(serialized_data,
                             {
             'name': 'Django',
            'domain':'Backend Development'
        }
                             )


class ProjectSerializerTestCase(TestCase):

    def test_valid_data(self):
        valid_data = {
                "title":"Alfabolt Analytics",
                "description":"",
                "start_date":"2023-08-08",
                "budget_in_dollars":400.00
        }
        serializer=ProjectSerializer(data=valid_data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors,{})
    def test_missing_required_field(self):
        missing_name ={

                "description":"",

                "budget_in_dollars":400.00
        }
        serializer = ProjectSerializer(data=missing_name)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors) 
        self.assertIn('start_date', serializer.errors) 

    def test_invalid_data(self):
        invalid_data = {
                "title":"Alfabolt Analytics",
                "description":"",
                "start_date":20230808,
                "budget_in_dollars":"400"
        }
        serializer=ProjectSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('start_date', serializer.errors)
       # self.assertIn("budget_in_dollars", serializer.errors)

    def test_output_data(self):
            output_data =  {
                "title":"Alfabolt Analytics",
                "description":"",
                "start_date":"2023-08-08",
                "budget_in_dollars":400.00
        }
            serializer=ProjectSerializer(data=output_data)
            self.assertTrue(serializer.is_valid())
            serialized_data=serializer.data
            self.assertEqual(serialized_data, {
                "title":"Alfabolt Analytics",
                "description":"",
                "start_date":"2023-08-08",
                "budget_in_dollars":"400.00"
        })
class ResourceProjectGetSerializerTestCase(TestCase):
    def test_serialization(self):
        resource = Resource.objects.create(first_name='John', last_name='Doe', email='john@example.com', designation='Software Engineer')
        project = Project.objects.create(title='Sample Project', description='A test project', start_date="2023-08-08", budget_in_dollars=400.00)
        project_resource = ProjectResource.objects.create(
            resource=resource,
            project=project,
            role='Backend',
            resource_joined_date='2023-08-15',
            project_lead=True,
        )

        serializer = ResourceProjectGetSerializer(instance=project_resource)

        # Get the serialized data
        serialized_data = serializer.data
        serialized_data_dict = dict(serialized_data)

        expected_data = {
                'resource': {
                'id':1,
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john@example.com',
                'designation': 'Software Engineer',
            },
            'project': {
                 'id':1,
                'title': 'Sample Project',
                'description': 'A test project',
                'start_date': '2023-08-08',
                'budget_in_dollars': '400.00',
            },

            'role': 'Backend',
            'resource_joined_date': '2023-08-15',
            'project_lead': True,
        }
        
        # Validate that the serialized data matches the expected data
        self.assertEqual(serialized_data_dict , expected_data)
