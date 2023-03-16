
from django import forms
from .models import *
from turtle import textinput
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Announcement

class LoginForm(forms.ModelForm):
    class Meta:
        model = checkLogin
        fields = ['username', 'password']
        widgets = {
            "username":  forms.TextInput(attrs={'placeholder':'','autocomplete': 'off'}), 
            "password": forms.PasswordInput(attrs={'placeholder':'','autocomplete': 'off','data-toggle': 'password'}),
        }
    
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['teachername', 'topic', 'announcement']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'username', 'passwd', 'classname', 'gradelvl']
    
    def save(self, commit=True):
        user = super(StudentForm, self).save(commit=False)
        if commit: user.save()
        return user
        
class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"
    
class HomeForm(forms.Form):
    post = forms.CharField()