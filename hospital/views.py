from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from hospital.models import Hospital
from hospital.hospital_serializer import HospitalSerializer


# Create your views here.
class HospitalOperations(ModelViewSet):
    queryset = Hospital.active_ent.all()
    serializer_class = HospitalSerializer


