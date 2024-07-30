from django.urls import path
from . import views


from employee.views import EmployeeViewSet

employee_list = EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', employee_list, name='employee_list'),
    path("<str:pk>/", employee_detail, name= 'employee_detail'),
]
    