from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_usuario.api import viewsets


router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewset, basename='Users')

urlpatterns = [
    # path('users/', users),
    path('api/', include(router.urls)),
    path('', include('frontend.urls')),
    
]
