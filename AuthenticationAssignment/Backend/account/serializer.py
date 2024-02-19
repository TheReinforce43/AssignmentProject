from rest_framework import serializers
from . models import StudentModel,TeacherModel,User
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username','email']

class StudentSignUpSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField(style={'input_type': 'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

class TeacherSignUpSerializer(serializers.ModelSerializer):
    password=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

  
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError({'error': 'Invalid username or password'})

        attrs['user'] = user
        return attrs