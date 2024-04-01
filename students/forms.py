from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
# from simple_forms.apps.core.models import Person

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = Student
#         fields = ('enrollment', 'name', 'email', 'password', 'mobile', 'dob', 'branch', 'gender')




class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('enrollment', 'name', 'email', 'password', 'mobile', 'dob', 'branch', 'gender')




 