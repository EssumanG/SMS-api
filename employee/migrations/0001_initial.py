# Generated by Django 5.0.6 on 2024-07-20 12:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee_number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('Plant Maintenance', 'Plant Maintenance'), ('Surface Maintenance', 'Surface Maintenance'), ('Property Maintenance and Construction', 'Property Maintenance and Construction'), ('Underground Maintenance', 'Underground Maintenance'), ('Underground Electricals', 'Underground Electricals'), ('Finance', 'Finance'), ('Geology', 'Geology'), ('Exploration', 'Exploration'), ('GSSOP', 'GSSOP'), ('Community', 'Community'), ('Human Resource', 'Human Resource'), ('Purchasing and Supply', 'Purchasing and Supply'), ('Security', 'Security'), ('Safety', 'Safety'), ('Environment', 'Environment'), ('Underground Mining', 'Underground Mining'), ('Technical Service', 'Technical Service'), ('Underground Service', 'Underground Service'), ('Information Technology', 'Information Technology'), ('Metallurgy', 'Metallurgy')], max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('telephone_number', models.CharField(max_length=20)),
            ],
        ),
    ]