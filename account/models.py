from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'admin'
        STUDENT = 'STUDENT', 'student'
        TEACHER = 'TEACHER', 'teacher'

    base_role = Role.ADMIN
    role = models.CharField(max_length=100, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)

class StudentModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    StudentName = models.CharField(max_length=250)
    Email = models.EmailField()
    Institute = models.CharField(max_length=250)
    Semester = models.IntegerField()
    RegistrationNumber = models.IntegerField()

    def __str__(self):
        return self.StudentName

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)

class Student(User):
    base_role = User.Role.STUDENT
    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return 'Only For Students'

class TeacherModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    TeacherName = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    ExperienceYear = models.IntegerField()

    def __str__(self):
        return self.TeacherName

class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)

class Teacher(User):
    base_role = User.Role.TEACHER
    teacher = TeacherManager()

    class Meta:
        proxy = True

    def welcome(self):
        return 'Only for Teachers'
