# Generated by Django 3.0 on 2020-02-17 13:44

import address.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import patient.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50, validators=[patient.models.check_gender])),
                ('birth_date', models.DateField()),
                ('blood_group', models.CharField(max_length=10, validators=[patient.models.check_blood_group])),
                ('diseases', models.CharField(max_length=100)),
                ('active', models.CharField(default='Y', max_length=1, validators=[address.models.check_active])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_ref', to='address.Address')),
                ('doctors', models.ManyToManyField(related_name='patient_ref', to='doctor.Doctor')),
            ],
            options={
                'db_table': 'Info_Patient',
            },
            managers=[
                ('all_ent', django.db.models.manager.Manager()),
            ],
        ),
    ]
