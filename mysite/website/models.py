from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50)
    passwd = models.CharField(max_length = 50)
    classname = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    
    def __str__(self): # what it returns
        return self.firstname + ' ' + self.lastname
