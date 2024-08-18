from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import IncidentReportSerializer, IncidentReportDetailSerialzer
from .models import IncidentReport
from rest_framework.response import Response
from rest_framework import status, mixins, filters
from rest_framework.pagination import PageNumberPagination
import datetime



# Create your views here.
class CreateListReportView(GenericAPIView):

    serializer_class = IncidentReportSerializer
    queryset = IncidentReport.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
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
    

    def post(self, request):
        

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