from django.shortcuts import render
from rest_framework import viewsets
from .models import AppointmentModel
from .serializers import AppointmentSerializer
# Create your views here.

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient')
        print(patient_id)
        if patient_id:
            queryset = queryset.filter(patient = patient_id)
        return queryset
    
