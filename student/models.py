from unittest.util import _MAX_LENGTH
from django.db import models

level_choices =[(1,1),(2,2),(3,3),(4,4)]
department_choices = [('General','General'),('AI','AI'),('CS','CS'),('IS','IS'),('IT','IT'),('DS','DS')]
status_choices =[('active','active'),('inactive','inactive')]
gender_choices = [('male','male'),('female','female')]


class student (models.Model):
    name = models.CharField(max_length =50, null=False)
    id =models.CharField(max_length=8, primary_key=True)
    level = models.SmallIntegerField( choices= level_choices)
    department = models.CharField(max_length=7, choices= department_choices)
    GPA = models.DecimalField(max_digits=3 , decimal_places=2)
    status = models.CharField(max_length=8, choices= status_choices)
    gender = models.CharField(max_length=6, choices= gender_choices)
    Email = models.CharField(max_length=20)
    Date_of_birth = models.DateField()
    phoneNumber = models.CharField(max_length=11)





