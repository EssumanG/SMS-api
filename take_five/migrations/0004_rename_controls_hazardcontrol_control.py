# Generated by Django 5.0.6 on 2024-07-19 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('take_five', '0003_rename_hazard_task_hazard_control_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hazardcontrol',
            old_name='controls',
            new_name='control',
        ),
    ]