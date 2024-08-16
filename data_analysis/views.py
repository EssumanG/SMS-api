from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q

from .serializers import DepartmentStatsSerializer, IncidentReportTrendSerializer

from employee.models import Employee
from take_five.models import Task
from incident_report.models import IncidentReport
# Create your views here.

class DepartmentStatsView(APIView):
    def get(self, request, *args, **kwargs):
        # List of all possible departments, including those not in Employee records
        all_departments = ['Property Maintenance and Construction', 'Surface Maintenance', 
                           'Plant Maintenance', 'Underground Maintenance', 
                           'Underground Electricals', 'Finance', 'Geology',
                           'Exploration', 'GSSOP', 'Community',
                           'Human Resource', 'Purchasing and Supply', 'Security',
                           'Safety', 'Environment', 'Underground Mining',
                           'Technical Service','Underground Service',
                            'Information Technology', 'Metallurgy']  # Extend this list as needed

        # Get existing department stats from employees
        department_stats = (
            Employee.objects.values('department')
            .annotate(
               take_five_count=Count('task_inittiator', filter=Q(task_inittiator__isnull=False)),
                incident_report_count=Count('reporter', filter=Q(reporter__isnull=False))
            )
            .order_by('department')
        )

        # Convert QuerySet to a dictionary for easy lookup
        department_stats_dict = {stat['department']: stat for stat in department_stats}

        # Build the complete list of department stats
        complete_stats = []
        for dept_name in all_departments:
            if dept_name in department_stats_dict:
                complete_stats.append(department_stats_dict[dept_name])
            else:
                # Add missing departments with zero counts
                complete_stats.append({'department': dept_name, 'take_five_count': 0, 'incident_report_count': 0})

        # Serialize the complete statistics
        serializer = DepartmentStatsSerializer(complete_stats, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    

class IncidentReportTrendView(APIView):

    def get(self, request, *args, **kwargs):
        # Group IncidentReports by the date_of_incident and count them
        queryset = IncidentReport.objects.values('date_of_incident').annotate(incident_count=Count('id')).order_by('date_of_incident')

        serializer = IncidentReportTrendSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)