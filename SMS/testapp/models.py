from django.db import models
from django.contrib.auth.models import AbstractUser
from .school import UserSchool



class User(models.Model):
    username=None
    school = models.CharField(max_length=500)
    studentgrade = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    is_verified = models.BooleanField(default=False)
    email = models.CharField(max_length=500, null=True, blank=True)
    forget_password = models.CharField(max_length=500, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    objects=UserSchool()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


     #School Model
class School(models.Model):
    School_id = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=500)
    studentclass = models.CharField(max_length=500)
    email = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500)
    pincode = models.CharField(max_length=500)
    password = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name + '--' + self.location


    #Student Model
class Student(models.Model):
        name = models.CharField(max_length=500)
        email = models.CharField(max_length=500)
        studentclass = models.CharField(max_length=500)
        rollno = models.CharField(max_length=500)
        studentgrade = models.CharField(max_length=500)


        #Student=models.ForeignKey(Student, on_delete=models.CASCADE)
