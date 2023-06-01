from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.core.validators import MaxValueValidator, MinValueValidator

CLASS_CHOICES = (
    ('sat 230', 'SAT 230'),
    ('sat 450', 'SAT 450'),
    ('ap calc 33', 'AP CALC 33'),
    ('algebra 1 130', 'ALGEBRA 1 130'),
    ('act 689', 'ACT 689'),
)

EXAM_CHOICES = (
    ('sat 230', 'SAT 230'),
    ('sat 450', 'SAT 450'),
    ('ap calc 33', 'AP CALC 33'),
    ('algebra 1 130', 'ALGEBRA 1 130'),
    ('act 689', 'ACT 689'),
)
class checkLogin(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
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
    # exam = models.CharField(max_length=20, choices=EXAM_CHOICES, default='sat 230')
    # test = models.ManyToManyField('Test', related_name="questions")
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
class Test(models.Model):
    title = models.CharField(max_length=200,null=True)
    questions = models.ManyToManyField(
        'QuesModel',
        related_name='Exams'
    )

    def __str__(self):
        return self.title
class Announcement(models.Model):
    teachername = models.CharField(max_length = 50, default="#")
    topic = models.CharField(max_length = 50, default="#")
    announcement = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.topic + ' by ' + self.teachername

class PdfTest(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')
    num_questions = models.PositiveIntegerField()
    answers = models.JSONField()
    def get_choices(self):
        # assuming each question has four answer choices, A, B, C, and D
        return [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
    def __str__(self):
        return self.name
     
     
     
class TeacherInquirie(models.Model):
    inqteacherfirstname = models.CharField(max_length = 50, default="#")
    inqteacherlastname = models.CharField(max_length = 50, default="#")
    inqteacheremail = models.EmailField(max_length = 200, default = "#")
    inqteachermessage = models.CharField(max_length = 500, default="#")
    
    def __str__(self):
        return self.inqteacherfirstname + ' ' + self.inqteacherlastname
    
class ToDoList(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item + ' | ' + str(self.completed)