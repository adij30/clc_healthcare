# Generated by Django 3.0 on 2020-02-17 13:44

import address.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('salary', models.FloatField(validators=[doctor.models.check_salary])),
                ('email', models.EmailField(max_length=50, validators=[doctor.models.check_email])),
                ('blog', models.SlugField(max_length=300)),
                ('active', models.CharField(default='Y', max_length=1, validators=[address.models.check_active])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_ref', to='hospital.Hospital')),
            ],
            options={
                'db_table': 'Info_Doctor',
            },
            managers=[
                ('all_ent', django.db.models.manager.Manager()),
            ],
        ),
    ]