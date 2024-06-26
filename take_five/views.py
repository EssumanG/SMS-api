from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics


# Create your views here.
class CreateListTask(GenericAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    get_serializer_class = GetTaskSerializer
    # empolyee_queryset = Employee.objects.all()
    # hazard_queryset = HazardControl.objects.all()

    def get(self, request):
        tasks = self.get_queryset()

        serializer = self.get_serializer_class(tasks, many = True)
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
    
class CreateListEmployee(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CreateListHazard(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = HazardControl.objects.all()
    serializer_class = HazardControlSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)