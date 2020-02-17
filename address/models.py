from django.db import models
from django.core.exceptions import ValidationError
import re


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='Y')


def check_active(value):
    if value not in ['Y', 'N']:
        raise ValidationError('Active value must be Y or N ...')


def check_pin_code(pin):
    r1 = re.fullmatch(r'^[1-9][0-9]{5}$', str(pin))
    if not r1:
        raise ValidationError('Enter valid Pincode ...')


class Address(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.IntegerField(validators=[check_pin_code])

    active = models.CharField(max_length=1, default='Y', validators=[check_active])

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    all_ent = models.Manager()
    active_ent = ActiveManager()

    class Meta:
        db_table = 'Info_Address'

    @property
    def adr(self):
        return self.city + ' - ' +self.state


'''
hospital doctor 	1 - M
hospital address	1 - 1
doctor 	patient		M - M 
patient address		M - 1
'''