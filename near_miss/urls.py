from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.CreateListNearMissView.as_view()),
    path('detail/<str:id>', views.NearMissDetailView.as_view()),
    path('employee/<str:id>/near_miss/', views.EmployeeNearMissById.as_view()),
]