# Generated by Django 5.0.6 on 2024-07-20 12:56

import datetime
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident_Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('time_of_incident', models.DateTimeField()),
                ('date_of_incident', models.DateField()),
                ('date_created', models.DateField(default=datetime.datetime.now)),
                ('statement', models.TextField()),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reporter', to='employee.employee')),
            ],
        ),
    ]