from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
# creating custom user manager
from datetime import time
class UserManager(BaseUserManager):
    def create_user(self, email, name,tc,user_type, password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
            user_type=user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,tc,user_type, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
            user_type=user_type,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# creating custom user
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    USER=(
        (1,"HOD"),
        (2,"STAFF"),
        (3,"STUDENT"),
        (4,"BRANCH"),
        (5,"ACCOUNTANT"),
        (6,"DEVELOPER"),
    )
    user_type=models.IntegerField(choices=USER,default=1)
    name = models.CharField(max_length=200)
    tc=models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","tc","user_type"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# creating a Class Model
class AddClass(models.Model):
    name=models.CharField(max_length=100)
    
    
#creating a shift Module
class Shift(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    
# College Name module
class College(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Grouptime(models.Model):
    groupname=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()
    location=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.groupname 
    

class Year(models.Model):
    date=models.CharField(max_length=100)
    def __str__(self):
        return self.date
    

    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration= models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Subject (models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    
class Branch(models.Model):
    bname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    open_date=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    