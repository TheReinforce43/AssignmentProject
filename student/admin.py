from django.contrib import admin
from student.models import StudentModel
# Register your models here.

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display =['id','StudentName','Email','Institute','Semester','RegistrationNumber']