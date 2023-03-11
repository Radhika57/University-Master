from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
    
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'           