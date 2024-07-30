from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import IncidentReportSerializer
from .models import IncidentReport
from rest_framework.response import Response
from rest_framework import status
import datetime



# Create your views here.
class CreateListView(GenericAPIView):

    serializer_class = IncidentReportSerializer
    queryset = IncidentReport.objects.all()

    def get(self):
        reports = self.get_queryset()

        serializer = self.serializer_class(reports, many = True)
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