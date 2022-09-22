from rest_framework import serializers
from MH_App.models.patientStatus import PatientStatus


class PatientStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientStatus
        fields = ['id', 'date', 'hour',
                  'paSystolic', 'paDiastolic', 'meanArterialPressure', 'heartRate', 'respiratoryRate', 'temperature']
