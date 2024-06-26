from django.urls import path
from . import views


urlpatterns = [
    path('take_five/', views.CreateListTask.as_view()),
    path('employee/', views.CreateListEmployee.as_view()),
    path('hazards/', views.CreateListHazard.as_view()),
    path('controls/', views.CreateListControl.as_view()),
]