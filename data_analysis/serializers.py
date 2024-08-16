from rest_framework import serializers


class DepartmentStatsSerializer(serializers.Serializer):
    department = serializers.CharField()
    take_five_count = serializers.IntegerField()
    incident_report_count = serializers.IntegerField()



class IncidentReportTrendSerializer(serializers.Serializer):
    date_of_incident = serializers.DateField()
    incident_count = serializers.IntegerField()