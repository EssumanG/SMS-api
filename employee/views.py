from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets, filters
# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'department', 'employee_number']

    # def get(self, request, *args, **kwargs):
    #     employees = self.get_queryset()
    #     print(request.headers)
    #     print("jijiji")
    #     # no_paginate = request.query_params.get('paginate').lower() == 'false'

    #     # if no_paginate:
    #     #     page = self.paginate_queryset(employees)

    #     #     if page is not None:
    #     #         serializer = self.get_serializer(page, many=True)
    #     #         return self.get_paginated_response(serializer.data)
            
    #     serializer = self.serializer_class(employees, many=True)
    #     response = {
    #         "msg": "list of all employees",
    #         "total": len(serializer.data),
    #         "data": serializer.data
    #     }

    #     return Response(response, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response( serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
