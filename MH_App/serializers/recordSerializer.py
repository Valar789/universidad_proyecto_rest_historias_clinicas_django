from rest_framework import serializers
from MH_App.models.record import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'diseasesHistory',
                  'medicationsHistory', 'medicalAllergies', 'familyHistory']
