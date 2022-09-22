from django.db import models
from .patient import Patient


class Record(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='record', on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    diseasesHistory = models.CharField(max_length=255)
    medicationsHistory = models.CharField(max_length=255)
    medicalAllergies = models.CharField(max_length=255)
    familyHistory = models.CharField(max_length=255)
