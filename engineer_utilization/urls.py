from django.urls import path
from . import views

urlpatterns = [
  
    #Project CRUD 
    path('project/',views.ProjectListCreateApiView.as_view()),
    path("project/<int:pk>/",views.ProjectDetailApiView.as_view()),
    path("project/<int:pk>/update/",views.ProjectUpdateApiView.as_view()),
    path("project/<int:pk>/delete/",views.ProjectDeleteApiView.as_view()),
    #Resource CRUD
    path('resource/',views.ResourceListCreateApiView.as_view()),
    path("resource/<int:pk>/",views.ResourceDetailApiView.as_view()),
    path("resource/<int:pk>/update/",views.ResourceUpdateApiView.as_view()),
    path("resource/<int:pk>/delete/",views.ResourceDeleteApiView.as_view()),

    #Technology CRUD
    path('technology/',views.TechnologyListCreateApiView.as_view()),
    path("technology/<int:pk>/",views.TechnologyDetailApiView.as_view()),
    path("technology/<int:pk>/update/",views.TechnologyUpdateApiView.as_view()),
    path("technology/<int:pk>/delete/",views.TechnologyDeleteApiView.as_view()),

    #Resource Technology CRUD
    path("resourcetechnology/resource/<int:id>/",views.GetResourceTechnologyListApiView.as_view()),
    path("resourcetechnology/technology/<int:id>/",views.GetTechnologyResourceListApiView.as_view()),
    path("resourcetechnology/",views.GetTechnologyResourceListApiView.as_view()),
    path("resourcetechnology/detail/<int:pk>/",views.ResourceTechDetailApiView.as_view()),
    path("resourcetechnology/<int:pk>/update/",views.ResourceTechUpdateApiView.as_view()),
    path("resourcetechnology/<int:pk>/delete/",views.ResourceTechDeleteApiView.as_view()),

    #--------------------------------Resource Project---------------------------------------------------------------------------------
    path("resourceproject/resource/<int:id>/",views.GetResourceProjectListApiView.as_view()),
    path("resourceproject/project/<int:id>/",views.GetProjectResourceListApiView.as_view()),
    path("resourceproject/",views.ProjectResourceCreateApiView.as_view()),
    path("resourceproject/detail/<int:pk>/",views.ProjectResourceDetailApiView.as_view()),
    path("resourceproject/<int:pk>/update/",views.ProjectResourceUpdateApiView.as_view()),
    path("resourceproject/<int:pk>/delete/",views.ProjectResourceDeleteApiView.as_view()),
   
 #--------------------------------------------------------------------------------------------------------------------------------------

]
