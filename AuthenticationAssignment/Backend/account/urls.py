from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('student/signup/',views.StudentSignUpView.as_view()),
    path('teacher/signup/',views.TeacherSignUpView.as_view()),
    path('login/',views.LoginView.as_view(),name='login'),
  
]
