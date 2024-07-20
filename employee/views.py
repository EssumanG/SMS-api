from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics
# Create your views here.


class CreateListEmployee(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)