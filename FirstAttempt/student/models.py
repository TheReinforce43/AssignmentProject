from django.db import models
from account.models import User
# Create your models here.
class StudentModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student',blank=True,null=True)
    StudentName = models.CharField(max_length=250)
    Email = models.EmailField()
    Institute = models.CharField(max_length=250,blank=True,null=True)
    Semester = models.IntegerField(blank=True,null=True)
    RegistrationNumber = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.StudentName