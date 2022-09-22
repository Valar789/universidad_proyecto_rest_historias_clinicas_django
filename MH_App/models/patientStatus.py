from datetime import timezone
from django.db import models
from .patient import Patient


def get_default_my_hour():
    hour = timezone.now()
    formatedHour = hour.strftime("%H:%M:%S")
    return formatedHour


class PatientStatus(models.Model):
    id = models.AutoField(primary_key=True),
    patient = models.ForeignKey(
        Patient, related_name='patientStatus', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    hour = models.CharField(max_length=20, default=get_default_my_hour)
    paSystolic = models.IntegerField()
    paDiastolic = models.IntegerField()
    meanArterialPressure = models.IntegerField(null=True, blank=True)
    heartRate = models.IntegerField()
    respiratoryRate = models.IntegerField()
    temperature = models.FloatField()
