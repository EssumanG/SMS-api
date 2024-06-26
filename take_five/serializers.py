from rest_framework import serializers
from .models import *
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class HazardControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = HazardControl
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    # serializers.ManyRelatedField
    # created_by =  EmployeeSerializer()
    # hazard = HazardControlSerializer(many=True)
    # other_workers = EmployeeSerializer(many=True)
    # supervisor = EmployeeSerializer()

    # hazard = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # created_by = serializers.PrimaryKeyRelatedField()
    # other_workers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # supervisor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class GetTaskSerializer(serializers.ModelSerializer):
    # serializers.ManyRelatedField
    created_by =  EmployeeSerializer()
    hazard = HazardControlSerializer(many=True)
    other_workers = EmployeeSerializer(many=True)
    supervisor = EmployeeSerializer()

    class Meta:
        model = Task
        fields = '__all__'
