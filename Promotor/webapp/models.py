from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.urls import reverse


class ProfilUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(ProfilUser, on_delete=models.CASCADE, primary_key=True, related_name='Teacher')
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    #messages = models.ManyToManyField(Student, through='StudentMessage')

    def get_absolute_url(self):
        return reverse('webapp:teacher_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=250)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(ProfilUser, on_delete=models.CASCADE, primary_key=True, related_name='Student')
    name = models.CharField(max_length=250)
    index = models.IntegerField()
    email = models.EmailField(max_length=254)
    group = models.ForeignKey(Group, null=True,blank=True, on_delete=models.DO_NOTHING)
    thesis = models.FileField(upload_to='uploads', null=True,blank=True)

    def get_absolute_url(self):
        return reverse('webapp:student_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class StudentMessage(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.DO_NOTHING, related_name='messages')
    student = models.ForeignKey(Student, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('teacher', 'student')
