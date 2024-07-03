from django.db import models
from patient.models import PatientModel
from doctor.models import DoctorModel,AvailableTime

# Create your models here.
APPOINTMENT_STATUS = (
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
)
APPOINTMENT_TYPES = (
    ('Offline','Offline'),
    ('Online','Online'),
)

class AppointmentModel(models.Model):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=30,choices=APPOINTMENT_TYPES)
    appointment_status = models.CharField(max_length=30,choices=APPOINTMENT_STATUS,default='Pending')
    time = models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    symptoms = models.TextField()

    def __str__(self):
        return f'Patient: {self.patient.user.first_name}, Doctor: {self.doctor.user.first_name}'
