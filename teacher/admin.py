from django.contrib import admin
from teacher.models import  TeacherModel 
# Register your models here.

@admin.register(TeacherModel)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id','TeacherName','Email','ExperienceYear']