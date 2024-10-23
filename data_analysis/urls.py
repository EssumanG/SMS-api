from django.urls import path
from .views import DepartmentStatsView, IncidentReportTrendView, DashboardView

urlpatterns = [
    path('department-stats/', DepartmentStatsView.as_view(), name='department-stats'),
    path('incident-trend/', IncidentReportTrendView.as_view(), name='incident-trend'),
    path('dashboard-info/', DashboardView.as_view(), name='dashboard-info')
]
