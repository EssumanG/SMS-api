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
            name='Control',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('control_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HazardControl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hazard_description', models.CharField(max_length=100)),
                ('control', models.ManyToManyField(to='take_five.control')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('question_empolyee', models.BooleanField(default=True)),
                ('question_competency', models.BooleanField(default=True)),
                ('question_tools_and_equip', models.BooleanField(default=True)),
                ('question_5A', models.BooleanField(null=True)),
                ('question_5B', models.BooleanField(null=True)),
                ('question_5C', models.BooleanField(null=True)),
                ('question_5D', models.BooleanField(null=True)),
                ('question_5E', models.BooleanField(null=True)),
                ('date_created', models.DateField(default=datetime.datetime.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_inittiator', to='employee.employee')),
                ('hazard_control_list', models.ManyToManyField(to='take_five.hazardcontrol')),
                ('other_workers', models.ManyToManyField(related_name='task_members', to='employee.employee')),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_supervisor', to='employee.employee')),
            ],
        ),
    ]
