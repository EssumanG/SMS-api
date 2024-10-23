from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.CreateListReportView.as_view()),
    path('detail/<str:id>', views.ReportDetailView.as_view()),
    path('employee/<str:id>/incident_reports/', views.EmployeeIncidentReportById.as_view()),
]