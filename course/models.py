from django.db import models
from category.models import CategoryModel

from account.models import StudentModel,TeacherModel
# Create your models here.

class CourseModel(models.Model):

    CourseName=models.CharField(max_length=250)
    Category=models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True)
    Duration=models.IntegerField(default=0)
    Teacher=models.ForeignKey(TeacherModel,on_delete=models.SET_NULL,null=True)
    TotalLecture=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.CourseName
    
    
class CourseEnrollment(models.Model):
    student=models.ForeignKey(StudentModel, related_name="Student",on_delete=models.SET_NULL)
    course=models.ForeignKey(CourseModel, related_name="Course", on_delete=models.SET_NULL)
    EnrolledTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.EnrolledTime




