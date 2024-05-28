from django.db import models
import uuid

# Create your models here.
class Employee (models.Model):
    employee_number = models.CharField(primary_key=True, max_length=100)
    name =  models.CharField(max_length=100)
    

class HazardControl(models.Model):
    harzard = models.CharField(max_length=100)
    risk = models.CharField(max_length = 100)
    control = models.CharField(max_length = 100)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.CharField(max_length=100)
    taskName = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='task_inittiator')
    other_workers = models.ManyToManyField(Employee, null=True, related_name='task_members')
    supervisor = models.ForeignKey(Employee, models.SET_NULL, null=True, related_name='task_supervisor')
    hazard = models.ManyToManyField(HazardControl)











