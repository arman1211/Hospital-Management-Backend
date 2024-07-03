from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import ServiceModel

# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
