from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django import forms

from .models import User, Teacher, Student, StudentMessage


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'answer'}),
            'password1': forms.PasswordInput(attrs={'class': 'answer'}),
            'password2': forms.PasswordInput(attrs={'class': 'answer'}),
        }


class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email']


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'index', 'email','thesis']


class MessageForm(forms.ModelForm):
    class Meta:
        model = StudentMessage
        fields = ['title', 'content']
