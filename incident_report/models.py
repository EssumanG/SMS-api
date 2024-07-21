from django.db import models
import uuid
import datetime
# Create your models here.
from take_five.models import Employee


class IncidentReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=50, null=False)
    time_of_incident = models.TimeField(null=False)
    date_of_incident = models.DateField(null=False)
    date_created = models.DateField(default=datetime.datetime.now)
    statement = models.TextField()
    reporter = models.ForeignKey(Employee, models.SET_NULL, null=True, related_name='reporter')