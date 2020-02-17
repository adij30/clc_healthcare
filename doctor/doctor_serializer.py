from rest_framework.serializers import ModelSerializer
from doctor.models import Doctor


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        # fields = '__all__'
        exclude = ('created_date', 'modified_date')
