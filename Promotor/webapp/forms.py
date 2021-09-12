from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms

from .models import User, Teacher, Student, StudentMessage, GroupNotice


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
        fields = ['name', 'index', 'email']


class MessageForm(forms.ModelForm):
    class Meta:
        model = StudentMessage
        fields = ['title', 'content']


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


class MessagesForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)
    file = forms.FileField()

class NoticeForm(forms.ModelForm):
    class Meta:
        model = GroupNotice
        fields = ['message']