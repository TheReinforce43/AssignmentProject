from rest_framework import serializers
from student.models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=['id','StudentName','Email','Institute','Semester','RegistrationNumber']


class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class StudentSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields = ['email', 'password', 'user_name', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self,validated_data):
            return StudentModel.objects.create_user(**validated_data)