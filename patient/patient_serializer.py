from rest_framework.serializers import ModelSerializer

from patient.models import Patient


class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
        # exclude = ('created_date', 'modified_date')
        fields = ('id', 'name', 'gender', 'birth_date', 'blood_group', 'diseases', 'active', 'age', 'doctors','address' )

