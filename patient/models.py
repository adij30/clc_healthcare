from django.db import models
from doctor.models import Doctor
from address.models import ActiveManager, Address, check_active
from django.core.exceptions import ValidationError


def check_blood_group(blood_group):
    blood_group_list = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
    if blood_group not in blood_group_list:
        raise ValidationError(f'''Enter a valid blood group name...
        example - {blood_group_list}''')


def check_gender(gender):
    gender_list = ['Male', 'Female']
    if gender not in gender_list:
        raise ValidationError(r'''
        Enter valid gender...
        example - Male or Female ''')


class Patient(models.Model):

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, validators=[check_gender])
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=10, validators=[check_blood_group])
    diseases = models.CharField(max_length=100)

    active = models.CharField(max_length=1, default='Y', validators=[check_active])

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    doctors = models.ManyToManyField(Doctor, related_name='patient_ref')

    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                related_name='patient_ref')

    all_ent = models.Manager()
    active_ent = ActiveManager()

    class Meta:
        db_table = 'Info_Patient'

    def age(self):
        import datetime
        dob = self.birth_date
        tod = datetime.date.today()
        my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
        return my_age

    age = property(age)


'''
hospital doctor 	1 - M
hospital address	1 - 1
doctor 	patient		M - M 
patient address		M - 1
'''