from django.db import models
from address.models import Address, ActiveManager
from address.models import check_active


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.BigIntegerField()

    active = models.CharField(max_length=1, default='Y', validators=[check_active])

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    address = models.OneToOneField(Address, on_delete=models.CASCADE,
                                   related_name='hospital_ref')

    all_ent = models.Manager()
    active_ent = ActiveManager()

    class Meta:
        db_table = 'Info_Hospital'


'''
hospital doctor 	1 - M
hospital address	1 - 1
doctor 	patient		M - M 
patient address		M - 1
'''

