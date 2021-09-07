from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView

from . import models
from . forms import UserForm
from .models import Group, Student


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('webapp:login')
    else:
        return render(request, 'webapp/login.html', {})


class StudentDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "student"
    model = models.Student
    template_name = 'webapp/student_detail_page.html'


## User Profile for teacher.
class TeacherDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "teacher"
    model = models.Teacher
    template_name = 'webapp/teacher_detail_page.html'


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



def group_students_list(request):
    query = request.GET.get("q", None)
    students = Group.objects.filter(teacher=request.user.Teacher)
    students_list = [x.student for x in students]
    qs = Student.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(name__icontains=query)
        )
    qs_one = []
    for x in qs:
        if x in students_list:
            qs_one.append(x)
        else:
            pass
    context = {
        "group_students_list": qs_one,
    }
    template = "webapp/group_students_list.html"
    return render(request, template, context)


class ClassStudentsListView(LoginRequiredMixin, DetailView):
    model = models.Teacher
    template_name = "webapp/group_students_list.html"
    context_object_name = "teacher"