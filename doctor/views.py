from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from doctor.models import Doctor
from doctor.doctor_serializer import DoctorSerializer

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class DoctorOperations(ModelViewSet):
    queryset = Doctor.active_ent.all()
    serializer_class = DoctorSerializer

    # authentication_classes = [JSONWebTokenAuthentication,]
    # permission_classes = [IsAuthenticated,]
