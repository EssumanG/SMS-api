from rest_framework import serializers


class DepartmentStatsSerializer(serializers.Serializer):
    department = serializers.CharField()
    take_five_count = serializers.IntegerField()
    incident_report_count = serializers.IntegerField()