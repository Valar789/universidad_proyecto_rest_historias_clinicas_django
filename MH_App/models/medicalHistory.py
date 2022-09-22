from django.db import models

from MH_App.models.patient import Patient


class Medicalhistory(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    treatingSpecialty = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    reasonForConsultation = models.CharField(max_length=100)
    diagnostic = models.CharField(max_length=100)
    medication = models.CharField(max_length=100)
    patient = models.ForeignKey(
        Patient, related_name='medicalHistory', on_delete=models.CASCADE, null=True, blank=True)
