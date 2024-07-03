from rest_framework.routers import DefaultRouter
from .views import SpecializationViewSet,DesignationViewSet,AvailableTimeViewSet,ReviewViewSet,DoctorViewSet
from django.urls import path,include

router = DefaultRouter()

router.register('list', DoctorViewSet)
router.register('specialization', SpecializationViewSet)
router.register('designation', DesignationViewSet)
router.register('available-time', AvailableTimeViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('',include(router.urls))
]
