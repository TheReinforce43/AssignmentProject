from django.contrib import admin
from . models import User,TeacherModel,StudentModel
# Register your models here.

admin.site.register(User)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)
