from django.contrib import admin
from enrollment.models import CourseEnrollment
# Register your models here.

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display =['course','student','course','EnrolledTime']
