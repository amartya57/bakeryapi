from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from userapp.api import views

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]