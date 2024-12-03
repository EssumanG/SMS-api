from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics, filters
from django_filters import rest_framework as djangoFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

class TaskFilter(djangoFilter.FilterSet):
    other_workers = djangoFilter.CharFilter(method='filter_other_workers')

    class Meta:
        model = Task
        fields = ['task_name', 'location', 'supervisor__name', 'supervisor__employee_number', 'created_by__name', 'created_by__employee_number']

    def filter_other_workers(self, queryset, name, value):
        return queryset.filter(other_workers__employee_number__icontains=value)
    

# Create your views here.
class CreateListTask(GenericAPIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [AllowAny]

    serializer_class = TaskSerializer 
    queryset = Task.objects.all()
    filterset_class = TaskFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['task_name', 'location', 'supervisor__name', 'supervisor__employee_number', 'created_by__name', 'created_by__employee_number', 'other_workers__employee_number']
    
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

class EmployeeTasksById(GenericAPIView):
    queryset = Task.objects.all()
    lookup_field = "id"
    filter_backends = [filters.SearchFilter]
    search_fields = ['task_name', 'location', 'supervisor__name', 'supervisor__employee_number', 'created_by__name', 'created_by__employee_number']
    # pagination_class = Page
    def get(self, request, *args, **kwargs):
        # Get the ID from the URL
        user_id = self.kwargs.get(self.lookup_field)
        if not user_id:
            return Response({"detail": "ID not provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filter tasks based on the conditions
        tasks = self.queryset.filter(
            Q(supervisor_id=user_id) |
            Q(created_by_id=user_id) |
            Q(other_workers__id=user_id)
        ).distinct()  # Ensure no duplicates if a task matches multiple criteria

        tasks = tasks.order_by('-date_created')

        page = self.paginate_queryset(tasks)
        if page is not None:
            serializer = TaskSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        # Serialize the filtered tasks
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
         


class CreateListHazard(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = HazardControl.objects.all()
    serializer_class = GetHazardControlSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hazard_description']
    pagination_class = None


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class CreateListControl(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['control_description']
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)