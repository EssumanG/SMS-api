from urllib.request import Request
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import IncidentReportSerializer, IncidentReportDetailSerialzer
from .models import IncidentReport
from rest_framework.response import Response
from rest_framework import status, mixins, filters
from rest_framework.pagination import PageNumberPagination
import datetime
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser



# Create your views here.
class CreateListReportView(GenericAPIView):

    serializer_class = IncidentReportSerializer
    queryset = IncidentReport.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    # parser_classes = (MultiPartParser, FormParser)
    search_fields = ['location', 'reporter__name', 'reporter__employee_number', 'reporter__department']

    def get(self, request):
        reports = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(reports)

        if page is not None:
            serializer = self.serializer_class(page, many = True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.serializer_class(reports, many=True)
        response = {
            "msg": "lists of all incident Reports",
            "total": len(serializer.data),
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)
    

    def post(self, request ):
        
        print(request.data)

        time_of_incident = request.data['time_of_incident']
        time_of_incident = datetime.datetime.strptime(time_of_incident, '%H:%M').time()
        request.data['time_of_incident'] = time_of_incident
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response( serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ReportDetailView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportDetailSerialzer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  
    


class EmployeeIncidentReportById(GenericAPIView):
    queryset = IncidentReport.objects.all()
    lookup_field = "id"
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        # Get the ID from the URL
        user_id = self.kwargs.get(self.lookup_field)
        if not user_id:
            return Response({"detail": "ID not provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filter tasks based on the conditions
        reports = self.queryset.filter(reporter=user_id)  # Ensure no duplicates if a task matches multiple criteria


        reports = reports.order_by('-date_created')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(reports, request)
        if page is not None:
            serializer = IncidentReportSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        
        # Serialize the filtered tasks
        serializer = IncidentReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)