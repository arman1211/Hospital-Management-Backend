from django.db import models
from django.contrib.auth.models import User
from patient.models import PatientModel
# Create your models here.
class Designation(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name
    
class Specialization(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)
    def __str__(self):
        return self.name
    
class AvailableTime(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class DoctorModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

RATING_CHOICES = (
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
)

class ReviewModel(models.Model):
    reviewer = models.ForeignKey(PatientModel, on_delete= models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.CharField(max_length=30, choices=RATING_CHOICES)

    def __str__(self):
        return f'Reviewer: {self.reviewer.user.first_name}, Doctor: {self.doctor.user.first_name}'