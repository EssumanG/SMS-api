from rest_framework import serializers
from .models import NearMiss
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class NearMissSerializer(serializers.ModelSerializer):
    reported_by = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True) 
    reported_by_name = serializers.SerializerMethodField()

    class Meta:
        model = NearMiss
        fields = ['id', 'location', 'time', 'date', 'hazard_class', 'reported_by_name', 'department', 'near_miss_description', 'action_taken', 'reported_by', 'unsafe_act', 'image']



    def get_reported_by_name(self, obj):
        return obj.reported_by.name if obj.reported_by else None
     
class NearMissDetailSerialzer(serializers.ModelSerializer):
    reported_by = EmployeeSerializer(read_only=True)


    class Meta:
        model = NearMiss
        fields = '__all__'