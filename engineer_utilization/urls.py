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
    path('tech/',views.TechnologyListCreateApiView.as_view()),
    path("tech/<int:pk>/",views.TechnologyDetailApiView.as_view()),
    path("tech/<int:pk>/update/",views.TechnologyUpdateApiView.as_view()),
    path("tech/<int:pk>/delete/",views.TechnologyDeleteApiView.as_view()),

    #Resource Technology CRUD
    path("restech/",views.ResourceTechListCreateApiView.as_view()),
    path("restech/<int:pk>/",views.ResourceTechDetailApiView.as_view()),
    path("restech/<int:pk>/update/",views.ResourceTechUpdateApiView.as_view()),
    path("restech/<int:pk>/delete/",views.ResourceTechDeleteApiView.as_view()),

    #Resource Project CRUD
    path("resproject/",views.ProjectResourceListCreateApiView.as_view()),
    path("resproject/<int:pk>/",views.ProjectResourceDetailApiView.as_view()),
    path("resproject/<int:pk>/update/",views.ProjectResourceUpdateApiView.as_view()),
    path("resproject/<int:pk>/delete/",views.ProjectResourceDeleteApiView.as_view()),
   


]
