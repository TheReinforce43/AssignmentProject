from rest_framework import serializers
from teacher.models import TeacherModel

class TeacherSerializer(serializers.ModelSerializer):
    model=TeacherModel
    fields=['id','TeacherName','Email','ExperienceYear']