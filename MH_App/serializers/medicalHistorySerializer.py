from rest_framework import serializers
from MH_App.models.medicalHistory import Medicalhistory


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicalhistory
        fields = ['id', 'treatingSpecialty', 'state',
                  'reasonForConsultation', 'diagnostic', 'medication']
