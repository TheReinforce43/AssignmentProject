from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self,email,first_name,last_name,user_name,password=None):
        if not email:
            raise ValueError('User Must have email')
        if not user_name:
            raise ValueError('User must have user_name')

        user=self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,first_name,last_name,user_name,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user 
    
    
class User(AbstractBaseUser):

    class Role(models.TextChoices):
        ADMIN = ('ADMIN', 'admin')
        STUDENT = ('STUDENT', 'student')
        TEACHER = ('TEACHER', 'teacher')
    user_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150,unique=True)
    phone_number=models.CharField(max_length=100,null=True)
    role=models.CharField(max_length=100,choices=Role.choices)

    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name','last_name']
    objects=UserManager()

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
    
    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin




