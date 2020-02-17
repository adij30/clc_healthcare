from django.db import models
from hospital.models import Hospital
from address.models import ActiveManager
from django.core.exceptions import ValidationError
from address.models import check_active


def check_salary(sal):
    if sal < 50000.0:
        raise ValidationError("Doctor salary can't be less than 50000.00 rupees...")


def check_email(email_id):
    if '@clc.in' not in email_id:
        raise ValidationError('Email id domain must be @clc.in ')


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    experience = models.IntegerField()
    salary = models.FloatField(validators=[check_salary])
    email = models.EmailField(max_length=50, validators=[check_email])
    blog = models.SlugField(max_length=300)

    active = models.CharField(max_length=1, default='Y', validators=[check_active])

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,
                                 related_name='doctor_ref')

    all_ent = models.Manager()
    active_ent = ActiveManager()

    class Meta:
        db_table = 'Info_Doctor'


'''
hospital doctor 	1 - M
hospital address	1 - 1
doctor 	patient		M - M 
patient address		M - 1
'''