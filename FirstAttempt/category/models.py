from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    CategoryName=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.CategoryName
    
