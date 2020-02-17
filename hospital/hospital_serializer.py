from rest_framework.serializers import ModelSerializer
from hospital.models import Hospital
from address.address_serializer import AddressSerializer


class HospitalSerializer(ModelSerializer):
    # address = AddressSerializer(many=False)
    class Meta:
        model = Hospital
        # fields = '__all__'
        exclude = ('created_date', 'modified_date')
