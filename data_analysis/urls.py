from django.urls import path
from .views import DepartmentStatsView

urlpatterns = [
    path('department-stats/', DepartmentStatsView.as_view(), name='department-stats'),
]
