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
    controls = models.ManyToManyField(Control)

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
    question_empolyee = models.BooleanField(null=False, default=True)
    question_competency = models.BooleanField(null=False, default=True)
    question_tools_and_equip = models.BooleanField(null=False, default=True)
    question_5A = models.BooleanField(null=True)
    question_5B = models.BooleanField(null=True)
    question_5C = models.BooleanField(null=True)
    question_5D = models.BooleanField(null=True)
    question_5E = models.BooleanField(null=True)



    def __repr__(self) -> str:
        return self.task_name
    

    def __str__(self) -> str:
        return self.task_name











