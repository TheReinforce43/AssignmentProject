from django.db import models
from account.models import User
# Create your models here.
class StudentModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    StudentName = models.CharField(max_length=250)
    Email = models.EmailField()
    Institute = models.CharField(max_length=250)
    Semester = models.IntegerField()
    RegistrationNumber = models.IntegerField()

    def __str__(self):
        return self.StudentName