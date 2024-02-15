from rest_framework import serializers
from student.models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    model=StudentModel
    fields=['id','StudentName','Email','Institute','Semester','RegistrationNumber']