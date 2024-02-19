from django.db import models
from account.models import User
# Create your models here.
class TeacherModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    TeacherName = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    ExperienceYear = models.IntegerField()

    def __str__(self):
        return self.TeacherName