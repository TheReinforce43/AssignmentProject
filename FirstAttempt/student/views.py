from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer,StudentSignUpSerializer,StudentLoginSerializer
from .models import StudentModel
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken


class StudentLoginView(APIView):
    def post(self,request):
        serializer=StudentLoginSerializer(data=request.data)

        if serializer.is_valid():

            email=serializer.validated_data['email']
            password=serializer.validated_data['password']

            user=authenticate(request,email=email,password=password)

            if user:
                refresh=RefreshToken.for_user(user)
                return Response({
                    'message':'Login successful',
                    'refresh':str(refresh),
                    'access': str(refresh.access_token),
                },
                status=status.HTTP_200_OK)
            
            else:
                return Response({'error':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class StudentSignupView(APIView):
    
    def post(self, request):

        serializer=StudentSignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


