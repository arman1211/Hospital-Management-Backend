from rest_framework import viewsets
from .serializers import DesignationSerializer,SpecializationSerializer,AvailableTimeSerializer,DoctorSerializer,ReviewSerializer
from .models import Specialization,Designation,AvailableTime,ReviewModel,DoctorModel

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializer


