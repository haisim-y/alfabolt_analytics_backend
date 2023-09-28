from django.urls import path
from . import views

urlpatterns = [
  
    #Project CRUD 
    path('',views.OutreachListCreateApiView.as_view()),
    path("<int:pk>/",views.OutreachDetailApiView.as_view()),
    path("<int:pk>/update/",views.OutreachUpdateApiView.as_view()),
    path("<int:pk>/delete/",views.OutreachDeleteApiView.as_view()),
    #Resource CRUD
]
