from django.shortcuts import render
from .models import ContactModel
from .serializer import ContactSerializer
from rest_framework import viewsets
# Create your views here.
class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer