from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics, filters


# Create your views here.
class CreateListTask(GenericAPIView):

    serializer_class = TaskSerializer 
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['task_name', 'location', 'supervisor__name', 'supervisor__employee_number', 'created_by__name', 'created_by__employee_number']
    
    # empolyee_queryset = Employee.objects.all()
    # hazard_queryset = HazardControl.objects.all()

    def get(self, request):
        tasks = self.filter_queryset(self.get_queryset())
        
        page = self.paginate_queryset(tasks)

        if page is not None:
            serializer = self.serializer_class(page, many = True)
            return self.get_paginated_response(serializer.data)
        

        serializer = self.serializer_class(tasks, many = True)
        response = {
            "msg": "lists of all tasks",
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        #take the response
        req = request.data

        

        serializer = self.serializer_class(data=req)
        if serializer.is_valid():
            serializer.save()

            return Response( serializer.data, status=status.HTTP_201_CREATED)
            

        #check if users and harzards are already in the database
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetailView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetialSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    


class CreateListHazard(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = HazardControl.objects.all()
    serializer_class = GetHazardControlSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hazard_description']


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class CreateListControl(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['control_description']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)