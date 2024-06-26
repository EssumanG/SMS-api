from django.db import models
import uuid

# Create your models here.
class Employee (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_number = models.CharField(max_length=100)
    name =  models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
    
class Control(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    control_description = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return self.control_description
    
    def __str__(self) -> str:
        return self.control_description
    


class HazardControl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    harzard_description = models.CharField(max_length=100)
    control = models.ManyToManyField(Control, null=False)

    def __repr__(self) -> str:
        return self.harzard_description
    
    def __str__(self) -> str:
        return self.harzard_description
    

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='task_inittiator')
    other_workers = models.ManyToManyField(Employee, related_name='task_members')
    supervisor = models.ForeignKey(Employee, models.SET_NULL, null=True, related_name='task_supervisor')
    hazard = models.ManyToManyField(HazardControl)

    def __repr__(self) -> str:
        return self.task_name
    

    def __str__(self) -> str:
        return self.task_name











