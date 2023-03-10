from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    #Primary key trong sql 
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, 
                            choices=[('student', 'Student'), ('faculty', 'Faculty'), ('administrator', 'Administrator')])
    class Meta:
        app_label = 'app'
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class PasswordResetCode(models.Model):
    code = models.CharField(max_length=6)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Course(models.Model):
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField
    credit = models.IntegerField()
    requirement = models.TextField()
    
    def __str__(self) -> str:
        return self.name
