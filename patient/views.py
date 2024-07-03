from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer,PatientRegistrationSerializer
from .models import PatientModel
# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer

class PatientRegistrationView(APIView):
    serializer_class = PatientRegistrationSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response('Form submission done')
        return Response(serializer.errors)
