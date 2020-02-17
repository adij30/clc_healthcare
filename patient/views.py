from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from patient.models import Patient
from patient.patient_serializer import PatientSerializer


# Create your views here.
class PatientOperations(ModelViewSet):
    queryset = Patient.active_ent.all()
    serializer_class = PatientSerializer


