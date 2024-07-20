from django.db import models
import uuid
import datetime

from employee.models import Employee
    
class Control(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    control_description = models.CharField(max_length=100, null=False)

    def __repr__(self) -> str:
        return self.control_description
    
    def __str__(self) -> str:
        return self.control_description
    


class HazardControl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hazard_description = models.CharField(max_length=100, null=False)
    control = models.ManyToManyField(Control)

    def __repr__(self) -> str:
        return self.hazard_description
    
    def __str__(self) -> str:
        return self.hazard_description
    


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name = models.CharField(max_length = 100, null=False)
    location = models.CharField(max_length = 100, null=False)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='task_inittiator')
    other_workers = models.ManyToManyField(Employee, related_name='task_members')
    supervisor = models.ForeignKey(Employee, models.SET_NULL, null=True, related_name='task_supervisor')
    hazard_control_list = models.ManyToManyField(HazardControl)
    question_empolyee = models.BooleanField(null=False, default=True)
    question_competency = models.BooleanField(null=False, default=True)
    question_tools_and_equip = models.BooleanField(null=False, default=True)
    question_5A = models.BooleanField(null=True)
    question_5B = models.BooleanField(null=True)
    question_5C = models.BooleanField(null=True)
    question_5D = models.BooleanField(null=True)
    question_5E = models.BooleanField(null=True)
    date_created = models.DateField(default=datetime.datetime.now)



    def __repr__(self) -> str:
        return self.task_name
    

    def __str__(self) -> str:
        return self.task_name











