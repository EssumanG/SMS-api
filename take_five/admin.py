from django.contrib import admin

# Register your models here.

from .models import *
from incident_report.models import IncidentReport

admin.site.register(Employee)
admin.site.register(HazardControl)
admin.site.register(Task)
admin.site.register(Control)
admin.site.register(IncidentReport)

