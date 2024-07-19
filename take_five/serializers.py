from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'

class HazardControlInputSerializer(serializers.ModelSerializer):
    control = ControlSerializer(many=True, read_only=True)
    control_id = serializers.PrimaryKeyRelatedField(queryset=Control.objects.all(),  write_only=True, many=True)
    hazard_id = serializers.UUIDField(write_only=True)
    serializers.UUIDField(write_only=True)

    class Meta:
        model = HazardControl
        fields = ['id', 'control', 'control_id', 'hazard_id', 'hazard_description']
        # fields = ['id', 'control', 'hazard_description']
        extra_kwargs = {
            'hazard_description': {'read_only': True},
        }

class HazardControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = HazardControl
        fields = '__all__'

    # def create(self, validated_data):
    #     print(validated_data)
    #     controls_data = validated_data.pop('control', [])
    #     print(validated_data)

    #     hazard_control = HazardControl.objects.create(**validated_data)

    #     hazard_control.control.set(controls_data)

    #     return hazard_control
        


# class TaskSerializer(serializers.ModelSerializer):
#     # created_by =  EmployeeSerializer()
#     # hazard = HazardControlSerializer(many=True)
#     # other_workers = EmployeeSerializer(many=True)
#     # supervisor = EmployeeSerializer()

#     hazard = serializers.PrimaryKeyRelatedField(many=True, queryset=HazardControlSerializer)
#     created_by = serializers.PrimaryKeyRelatedField(queryset=EmployeeSerializer, read_only=True)
#     other_workers = serializers.PrimaryKeyRelatedField(many=True, queryset=EmployeeSerializer)
#     supervisor = serializers.PrimaryKeyRelatedField(queryset=EmployeeSerializer)

#     class Meta:
#         model = Task
#         fields = ['id','task_name', 'location', 'created_by', 'other_workers', 'supervisor', 'hazard', 'question_empolyee', 'question_competency', 'question_tools_and_equip', 'question_5A', 'question_5B', 'question_5C', 'question_5D', 'question_5E']


class TaskSerializer(serializers.ModelSerializer):
    # For reading nested relationships
    created_by = EmployeeSerializer(read_only=True)
    hazard_control_list = HazardControlSerializer(many=True, read_only=True)
    other_workers = EmployeeSerializer(many=True, read_only=True)
    supervisor = EmployeeSerializer(read_only=True)

    # For writing nested relationships using primary keys
    created_by_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),  write_only=True)
    hazard_control_list_id = HazardControlInputSerializer(many=True, write_only=True)
    other_workers_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),  many=True, write_only=True)
    supervisor_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),  write_only=True)

    class Meta:
        model = Task
        fields =  ['id','task_name', 'location', 'created_by', 'created_by_id', 'other_workers', 'other_workers_id','supervisor', 'supervisor_id', 'hazard_control_list', 'hazard_control_list_id', 'question_empolyee', 'question_competency', 'question_tools_and_equip', 'question_5A', 'question_5B', 'question_5C', 'question_5D', 'question_5E']
        # fields =  ['id','task_name', 'location', 'created_by', 'other_workers','supervisor', 'hazard_control_list', 'question_empolyee', 'question_competency', 'question_tools_and_equip', 'question_5A', 'question_5B', 'question_5C', 'question_5D', 'question_5E']
        
        extra_kwargs = {
            'created_by': {'read_only': True},
            'hazard_control_list': {'read_only': True},
            'other_workers': {'read_only': True},
            'supervisor': {'read_only': True},
        }

    def create(self, validated_data):
        print(validated_data)
        hazard_controls_list = validated_data.pop('hazard_control_list_id', [])
        other_workers = validated_data.pop('other_workers_id', [])
        created_by = validated_data.pop('created_by_id')
        supervisor = validated_data.pop('supervisor_id')
        print(hazard_controls_list, other_workers)
        print(validated_data)

        task = Task.objects.create(
            created_by=created_by,
            supervisor=supervisor,
            **validated_data
        )
        task.other_workers.set(other_workers)
        # task.created_by.add(created_by)
        # task.supervisor.add(supervisor)
        print(task)
        for hazard_control_data in hazard_controls_list:
            print(hazard_control_data)
            controls = hazard_control_data.pop('control_id')
            hazard_id = hazard_control_data.get('hazard_id')
            print("harzard------", hazard_id)
            hazard = HazardControl.objects.get(pk=hazard_id)
            hazard.control.set(controls)
            task.hazard_control_list.add(hazard)
        return task
    

class GetHazardControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = HazardControl
        fields = ['id', 'hazard_description']

class GetTaskSerializer(serializers.ModelSerializer):
    # serializers.ManyRelatedField
    created_by =  EmployeeSerializer()
    hazard = HazardControlSerializer(many=True)
    other_workers = EmployeeSerializer(many=True)
    supervisor = EmployeeSerializer()

    class Meta:
        model = Task
        fields = '__all__'
