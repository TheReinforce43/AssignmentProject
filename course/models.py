from django.db import models
from category.models import CategoryModel

from teacher.models import TeacherModel
# Create your models here.

class CourseModel(models.Model):

    CourseName=models.CharField(max_length=250)
    Category=models.OneToOneField(CategoryModel,on_delete=models.SET_NULL,null=True)
    Duration=models.IntegerField(default=0)
    Teacher=models.ForeignKey(TeacherModel,on_delete=models.SET_NULL,null=True)
    TotalLecture=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.CourseName
    





