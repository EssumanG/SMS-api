from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import IncidentReportSerializer
from .models import IncidentReport
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class CreateListView(GenericAPIView):

    serializer_class = IncidentReportSerializer
    queryset = IncidentReport.objects.all()

    def get(self, request):
        reports = self.get_queryset()

        serializer = self.serializer_class(reports, many = True)
        response = {
            "msg": "lists of all incident Reports",
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)
    

    def post(self, request):
        #take the response
        req = request.data

    # TODO: check the date and time befor saving
        serializer = self.serializer_class(data=req)
        if serializer.is_valid():
            serializer.save()

            return Response( serializer.data, status=status.HTTP_201_CREATED)
            
        #check if users and harzards are already in the database
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)