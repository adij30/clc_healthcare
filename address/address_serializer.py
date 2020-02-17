from rest_framework.serializers import ModelSerializer
from address.models import Address


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        # fields = '__all__'
        exclude = ('created_date', 'modified_date')
