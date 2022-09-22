from rest_framework import serializers
from MH_App.models.patient import Patient
from MH_App.models.medicalHistory import Medicalhistory
from MH_App.models.patientStatus import PatientStatus
from MH_App.models.record import Record
from .medicalHistorySerializer import MedicalHistorySerializer
from .patientStatusSerializer import PatientStatusSerializer
from .recordSerializer import RecordSerializer


class PatientSerializer(serializers.ModelSerializer):

    medicalHistory = MedicalHistorySerializer(many=True)
    patientStatus = PatientStatusSerializer(many=True)
    record = RecordSerializer(many=True)

    class Meta:
        model = Patient
        fields = "__all__"

    def create(self, validated_data):
        medicalHistoryData = validated_data.pop('medicalHistory')
        patientStatusData = validated_data.pop('patientStatus')
        recordData = validated_data.pop('record')
        patientInstance = Patient.objects.create(**validated_data)

        for data in medicalHistoryData:
            Medicalhistory.objects.create(patient=patientInstance, **data)

        for data in patientStatusData:
            PatientStatus.objects.create(patient=patientInstance, **data)

        for data in recordData:
            Record.objects.create(patient=patientInstance, **data)

        return patientInstance

    def update(self, instance, validated_data):
        medicalHistoryList = validated_data.pop('medicalHistory')
        patientStatusList = validated_data.pop('patientStatus')
        recordList = validated_data.pop('record')
        instance.namePatient = validated_data.get(
            'namePatient', instance.namePatient)
        instance.documentPatient = validated_data.get(
            'documentPatient', instance.documentPatient)
        instance.phonePatient = validated_data.get(
            'phonePatient', instance.phonePatient)
        instance.address = validated_data.get('address', instance.address)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.birthDate = validated_data.get(
            'birthDate', instance.birthDate)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.bloodType = validated_data.get(
            'bloodType', instance.bloodType)
        instance.financier = validated_data.get(
            'financier', instance.financier)
        instance.ethnicGroup = validated_data.get(
            'ethnicGroup', instance.ethnicGroup)
        instance.patientType = validated_data.get(
            'patientType', instance.patientType)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.entryDate = validated_data.get(
            'entryDate', instance.entryDate)
        instance.exitDate = validated_data.get('exitDate', instance.exitDate)
        instance.registerDate = validated_data.get(
            'registerDate', instance.registerDate)
        instance.save()

        medicalHistoryWithSameInstance = Medicalhistory.objects.filter(
            patient=instance.pk).values_list('id', flat=True)
        medicalHistoryIdPool = []
        for data in medicalHistoryList:
            if id in data.keys():
                if Medicalhistory.objects.filter(id=data['id']).exists():
                    medicalHistoryInstance = Medicalhistory.objects.get(
                        id=data['id'])
                    medicalHistoryInstance.treatingSpecialty = data.get(
                        'treatingSpecialty', medicalHistoryInstance.treatingSpecialty)
                    medicalHistoryInstance.save()
                    medicalHistoryIdPool.append(medicalHistoryInstance.id)
                else:
                    continue
            else:
                medicalHistoryInstance = Medicalhistory.objects.create(
                    patient=instance, **data)
                medicalHistoryIdPool.append(medicalHistoryInstance.id)
            for dataId in medicalHistoryWithSameInstance:
                if dataId not in medicalHistoryIdPool:
                    Medicalhistory.objects.filter(pk=dataId).delete()

        recordWithSameInstance = Record.objects.filter(
            patient=instance.pk).values_list('id', flat=True)
        recordIdPool = []
        for data in recordList:
            recordInstance = Record.objects.create(
                patient=instance, **data)
            recordIdPool.append(recordInstance.id)
            for dataId in recordWithSameInstance:
                if dataId not in recordIdPool:
                    Record.objects.filter(pk=dataId).delete()

        patientStatusWithSameInstance = PatientStatus.objects.filter(
            patient=instance.pk).values_list('id', flat=True)
        patientStatusIdPool = []
        for data in patientStatusList:
            patientStatusInstance = PatientStatus.objects.create(
                patient=instance, **data)
            patientStatusIdPool.append(patientStatusInstance.id)
            for dataId in patientStatusWithSameInstance:
                if dataId not in patientStatusIdPool:
                    PatientStatus.objects.filter(pk=dataId).delete()
        return instance
