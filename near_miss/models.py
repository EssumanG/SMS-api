from django.db import models
from django.db import models
import uuid
import datetime
# Create your models here.
from take_five.models import Employee
# Create your models here.



class NearMiss(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=50, null=False)
    time = models.TimeField(null=False)
    date = models.DateField(null=False)
    date_created = models.DateField(default=datetime.datetime.now)
    department = models.CharField(max_length=255, null=False)
    hazard_class = models.CharField(max_length=255, null=False)
    unsafe_act = models.CharField(max_length=255, null=False)
    near_miss_description = models.TextField()
    action_taken = models.TextField()
    reported_by = models.ForeignKey(Employee, models.SET_NULL, null=True, related_name='reported_by')
    image = models.ImageField(upload_to='near_miss', null=True)

    class Meta:
        ordering = ['date']