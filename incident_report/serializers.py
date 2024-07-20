from rest_framework import serializers
from .models import IncidentReport
from employee.models import Employee

class IncidentReportSerializer(serializers.ModelSerializer):

    reporter = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all()) 

    class Meta:
        model = IncidentReport
        fields = ['id', 'location', 'time_of_incident', 'date_of_incident', 'statement', 'reporter']