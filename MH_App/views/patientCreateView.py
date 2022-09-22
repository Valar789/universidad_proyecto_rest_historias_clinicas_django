from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from MH_App.models.patientStatus import PatientStatus
from MH_App.models import patient
from MH_App.serializers.patientSerializer import PatientSerializer
from MH_App.models.patient import Patient


class PatientCreateView(views.APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Patient.objects.all()
        # patient = PatientStatus.objects.all()
        serializer = PatientSerializer(post,  many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
