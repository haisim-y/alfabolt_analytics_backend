from django.urls import resolve, reverse
from rest_framework.test import APITestCase
from rest_framework import status
from . import views
class URLtestCaseGetResource(APITestCase):

    def test_url_mapping_resolve(self):
        url=reverse('resource')
        #It matches url with the view func 
        resolver_match=resolve(url)
        #Getiing view func obj
        view_func=resolver_match.func
        #getting class based view 
        view_class=view_func.cls

        self.assertEqual(view_class.__name__,'ResourceListCreateApiView')

class URLtestCasePostResource(APITestCase):

    def test_url_mapping_resolve(self):
        url=reverse('resource_detail',args=[1])
        #It matches url with the view func 
        resolver_match=resolve(url)
        #Getiing view func obj
        view_func=resolver_match.func
        #getting class based view 
        view_class=view_func.cls

        self.assertEqual(view_class.__name__,'ResourceDetailApiView')

class URLtestCaseUpdateResource(APITestCase):

    def test_url_mapping_resolve(self):
        url=reverse('resource_update',args=[1])
        #It matches url with the view func 
        resolver_match=resolve(url)
        #Getiing view func obj
        view_func=resolver_match.func
        #getting class based view 
        view_class=view_func.cls

        self.assertEqual(view_class.__name__,'ResourceUpdateApiView')

class URLtestCaseDeleteResource(APITestCase):

    def test_url_mapping_resolve(self):
        url=reverse('resource_delete',args=[1])
        #It matches url with the view func 
        resolver_match=resolve(url)
        #Getiing view func obj
        view_func=resolver_match.func
        #getting class based view 
        view_class=view_func.cls

        self.assertEqual(view_class.__name__,'ResourceDeleteApiView')

class URLtestCaseGetDetailResource(APITestCase):

    def test_url_mapping_resolve(self):
        url=reverse('resource_detail',args=[1])
        #It matches url with the view func 
        resolver_match=resolve(url)
        #Getiing view func obj
        view_func=resolver_match.func
        #getting class based view 
        view_class=view_func.cls

        self.assertEqual(view_class.__name__,'ResourceDetailApiView')