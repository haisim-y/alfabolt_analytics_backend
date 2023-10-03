from django.urls import path
from . import views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
        path('registration/',views.UserRegistration.as_view()),
        path('login/',views.UserLogin.as_view()),
        path('token/refresh/',views.TokenRefreshView.as_view()),
        #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('<int:pk>/update/',views.UserUpdateView.as_view()),
        path('<int:pk>/delete/',views.UserDestroyView.as_view()),
        path('<int:pk>/',views.UserDetailView.as_view())
]