from rest_framework import serializers
from .models import IncidentReport
from employee.models import Employee
from employee.serializers import EmployeeSerializer

class IncidentReportSerializer(serializers.ModelSerializer):

    reporter = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True) 
    reported_by_name = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    class Meta:
        model = IncidentReport
        fields = ['id', 'location', 'time_of_incident', 'date_of_incident', 'statement', 'reported_by_name', 'department', 'reporter', 'image']



    def get_reported_by_name(self, obj):
        return obj.reporter.name if obj.reporter else None
    
    def get_department(self, obj):
        return obj.reporter.department if obj.reporter else None
    

class IncidentReportDetailSerialzer(serializers.ModelSerializer):
    reporter = EmployeeSerializer(read_only=True)


    class Meta:
        model = IncidentReport
        fields = '__all__'

        # extra_kwards = {'repoerter_name':{'read_only': True}}


