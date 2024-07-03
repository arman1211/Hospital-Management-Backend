from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import PatientViewSet,PatientRegistrationView

router = DefaultRouter()

router.register('list',PatientViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register',PatientRegistrationView.as_view(),name='register'),
]
