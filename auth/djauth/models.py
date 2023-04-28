from django.db import models
from django.contrib.auth.models import User

class checkLogin(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
class Student(models.Model):
    username = models.CharField(max_length = 50)
    passwd = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 100)
    classname = models.CharField(max_length = 100)
    gradelvl = models.CharField(max_length=100)
    def __str__(self): # what it returns
        return self.username
    
class Teacher(models.Model):
    username = models.CharField(max_length = 50)
    passwd = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 100)
    prefix = models.CharField(max_length = 50)
    classname = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    
    def __str__(self): # what it returns
        return self.firstname + ' ' + self.lastname
# Create your models here.


class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
class Announcement(models.Model):
    teachername = models.CharField(max_length = 50, default="#")
    topic = models.CharField(max_length = 50, default="#")
    announcement = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.topic + ' by ' + self.teachername
    
    
    