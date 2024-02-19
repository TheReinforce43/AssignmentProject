from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username
    

class StudentModel(models.Model):
    student=models.OneToOneField(User, related_name='student',on_delete=models.SET_NULL,null=True,blank=True)
    StudentName = models.CharField(max_length=250,null=True, blank=True)
    Email = models.EmailField()
    Institute = models.CharField(max_length=250,null=True, blank=True)
    Semester = models.IntegerField(null=True, blank=True)
    RegistrationNumber = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.student.username
    
class TeacherModel(models.Model):
    teacher=models.OneToOneField(User,related_name="teacher",on_delete=models.SET_NULL,null=True,blank=True)
    TeacherName = models.CharField(max_length=250,null=True,blank=True)
    Email = models.EmailField()
    ExperienceYear = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.teacher.username


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender=settings.AUTH_USER_MODEL,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)