from django.contrib import admin
from .models import CourseModel
# Register your models here.

@admin.register(CourseModel)

class CourseModelAdmin(admin.ModelAdmin):
    list_display =['id','CourseName','Category','Duration','Teacher','TotalLecture']
