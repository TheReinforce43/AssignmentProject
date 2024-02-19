from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from . serializer import UserSerializer,StudentSignUpSerializer,TeacherSignUpSerializer,LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from . models import StudentModel,TeacherModel,User
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.settings import api_settings
from .permissions import isStudentUser,isTeacherUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.status import HTTP_201_CREATED
from rest_framework.authentication import TokenAuthentication

class StudentSignUpView(generics.CreateAPIView):
    serializer_class = StudentSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=self.perform_create(serializer)
        
        return Response({
            'user':UserSerializer(
                user,context=self.get_serializer_context()
            ).data,
            'token':Token.objects.get(user=user).key,
            'message':'Student Account Created Succesfully'
        })

    def get_queryset(self):
        return User.objects.none()
    
    def perform_create(self, serializer):
        user = serializer.save()
        user.is_student = True
        user.save()

        try:
            student_data = {
                'student': user,
                'StudentName': serializer.validated_data.get('username'),
                'Email': serializer.validated_data.get('email')
            }

            StudentModel.objects.create(**student_data)
            return user
        except Exception:
            user.delete()
            raise serializers.ValidationError("Student creation failed due to a conflict.")
    
class TeacherSignUpView(generics.CreateAPIView):
   
   serializer_class=TeacherSignUpSerializer

   def post(self,request,*args, **kwargs):
       serializer=self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       user=self.perform_create(serializer)

       return Response({
         'user':UserSerializer(user,context=self.get_serializer_context()).data,
         'token':Token.objects.get(user=user).key,
         'message':'Teacher Account Created Successfully'  
       })
    
   def get_queryset(self):
        return User.objects.none()

   def perform_create(self,serializer):
       user=serializer.save()
       user.is_teacher=True
       user.save()
       try:
           teacher_data={
               'teacher':user,
               'TeacherName':serializer.validated_data.get('username'),
               'Email':serializer.validated_data.get('email')
           }
           TeacherModel.objects.create(**teacher_data)
           return user
       except Exception:
           user.delete()
     
           raise serializers.ValidationError("Invalid Teacher creation")
   


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        role = "Student" if user.is_student else "Teacher"
        
        return Response({
            'user': user.username,
            'token': token.key,
            'message': 'Login successful!',
            'role': role
        }, status=status.HTTP_200_OK)
