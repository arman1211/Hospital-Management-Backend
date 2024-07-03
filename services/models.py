from django.db import models

# Create your models here.

class ServiceModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='services/images/')