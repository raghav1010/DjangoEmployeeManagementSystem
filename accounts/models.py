from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from django.contrib.auth.models import User

class Employee(User):

    DEPT=[
        ('HR','HR'),
        ('Sales','Sales'),
        ('Cloud','Cloud'),
        ('AI','AI'),
        ('Devops','Devops'),
        ('Backend','Backend'),
        ('UI','UI'),
        ('QA','QA')
    ]

    ROLE= [
        ('Intern','Inter'),
        ('Software_Engineer','Software_Engineer'),
        ('Senior_Engineer','Senior_Engineer'),
        ('Manager','Manager'),
        ('Executive','Executive')
    ]

    GENDER= [
        ('Female','Female'),
        ('Male','Male'),
      
    ]
    status = "emp"
    
    name = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    gender = models.CharField(max_length=50, choices=GENDER, default='Female')
    DOB = models.DateField(default='1998-01-01')
    role = models.CharField(choices=ROLE,max_length=100)
    dept = models.CharField(choices= DEPT,max_length=100)
    leave_count=3
    class Meta:
         
        db_table = 'employee'

    def __str__(self):
        return self.status



class System(User):

    status = "ad"
    
    class Meta:
         
        db_table = 'system'

    def __str__(self):
        return self.status

    
class Leave(models.Model):
    STATUS= [
        ('Approved','Approved'),
        ('Declined','Declined'),
        ('Wait',"Wait"),
      
    ]
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    startdate = models.DateField(default='2021-05-26')
    enddate = models.DateField(default='2021-05-26')
    name = models.CharField(max_length=20)
    
    status = models.CharField(choices=STATUS,max_length=20,default='Wait')


    def __str__(self):
        return self.name 
