from app_usuario.api import serializers
from rest_framework import viewsets
from app_usuario import models

class UserViewset(viewsets.ModelViewSet):
  serializer_class = serializers.UserSerializers
  queryset=models.User.objects.all()
  
