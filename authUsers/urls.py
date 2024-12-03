from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAuthuser.as_view()),
    path('login/', views.LoginAuthUser.as_view()),
    
]