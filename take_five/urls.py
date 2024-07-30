from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateListTask.as_view()),
    path('<str:id>/', views.TaskDetailView.as_view()),
    path('hazards/', views.CreateListHazard.as_view()),
    path('controls/', views.CreateListControl.as_view()),
]