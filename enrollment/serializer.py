from rest_framework import serializers
from enrollment.models import CourseEnrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    model=CourseEnrollment
    fields=['id','student','course']