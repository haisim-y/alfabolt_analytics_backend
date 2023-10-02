from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.PostListCreateApiView.as_view()),
    path("post/<int:pk>/",views.PostDetailApiView.as_view()),
    path("post/<int:pk>/update/",views.PostUpdateApiView.as_view()),
    path("post/<int:pk>/delete/",views.PostDeleteApiView.as_view()),

    path('lead/',views.LeadListCreateApiView.as_view()),
    path("lead/<int:pk>/",views.LeadDetailApiView.as_view()),
    path("lead/<int:pk>/update/",views.LeadUpdateApiView.as_view()),
    path("lead/<int:pk>/delete/",views.LeadDeleteApiView.as_view()),
]
