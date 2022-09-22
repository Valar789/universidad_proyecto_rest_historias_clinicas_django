from django.contrib import admin
from .models.medicalHistory import Medicalhistory
from .models.patient import Patient
from .models.patientStatus import PatientStatus
from .models.user import User
from .models.record import Record

# Register your models here.
admin.site.register(User)
admin.site.register(Record)
admin.site.register(Patient)
admin.site.register(PatientStatus)
admin.site.register(Medicalhistory)
