from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse


class ProfilUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(ProfilUser, on_delete=models.CASCADE, primary_key=True, related_name='Student')
    name = models.CharField(max_length=250)
    index = models.IntegerField()
    email = models.EmailField(max_length=254)

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(ProfilUser, on_delete=models.CASCADE, primary_key=True, related_name='Teacher')
    name = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    class_students = models.ManyToManyField(Student, through="StudentsInClass")

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class StudentsInClass(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="class_teacher", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="user_student_name", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:
        unique_together = ('teacher', 'student')
