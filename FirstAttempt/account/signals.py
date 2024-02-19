from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Student, Teacher, StudentModel, TeacherModel

@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'STUDENT':
        StudentModel.objects.create(user=instance)

@receiver(post_save, sender=Teacher)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'TEACHER':
        TeacherModel.objects.create(user=instance)
