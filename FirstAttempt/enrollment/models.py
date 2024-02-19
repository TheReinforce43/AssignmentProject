from django.db import models
from course.models import CourseModel
from student.models import StudentModel
# Create your models here.
    
class CourseEnrollment(models.Model):
    student=models.ForeignKey(StudentModel, related_name="Student",on_delete=models.SET_NULL,null=True,blank=True)
    course=models.ForeignKey(CourseModel, related_name="Course", on_delete=models.SET_NULL,null=True,blank=True)
    EnrolledTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.EnrolledTime