from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateListEmployee.as_view()),
]
    