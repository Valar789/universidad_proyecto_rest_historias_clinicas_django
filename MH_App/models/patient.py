from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    namePatient = models.CharField(max_length=100)
    documentPatient = models.IntegerField()
    phonePatient = models.IntegerField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    birthDate = models.DateTimeField()
    sex = models.CharField(max_length=30)
    bloodType = models.CharField(max_length=30)
    financier = models.CharField(max_length=30)
    ethnicGroup = models.CharField(max_length=30)
    patientType = models.CharField(max_length=30)
    weight = models.FloatField()
    height = models.FloatField()
    entryDate = models.DateTimeField()
    exitDate = models.DateTimeField()
    registerDate = models.DateTimeField(auto_now_add=True)

    # def save(self, **kwargs):
    #     super().save(**kwargs)
    USERNAME_FIELD = 'patient'
