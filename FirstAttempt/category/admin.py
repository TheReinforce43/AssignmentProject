from django.contrib import admin
from .models import CategoryModel
# Register your models here.

@admin.register(CategoryModel)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','CategoryName']
