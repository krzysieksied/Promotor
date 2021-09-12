from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.models import User

from . import models
from .forms import UserForm, ThreadForm, MessagesForm, NoticeForm
from .models import Group, Student, ThreadModel, MessageModel


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

    teacher_group = Group.objects.filter(teacher=request.user.profile.Teacher).first()
    students_list = [student for student in teacher_group.students.all()]
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


class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads
        }

        return render(request, 'webapp/inbox.html', context)


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form': form
        }

        return render(request, 'webapp/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('webapp:thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('webapp:thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('webapp:thread', pk=thread.pk)
        except:
            return redirect('webapp:create-thread')


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessagesForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }

        return render(request, 'webapp/thread.html', context)


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message'),
            file=request.FILES.get('file')
        )

        message.save()
        return redirect('webapp:thread', pk=pk)


def StudentMessage(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    receiver = User.objects.get(username=student.user)
    if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
        thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
        return redirect('webapp:thread', pk=thread.pk)
    elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
        thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
        return redirect('webapp:thread', pk=thread.pk)


@login_required
def add_notice(request):
    notice_sent = False
    teacher = request.user.profile.Teacher
    teacher_group = Group.objects.filter(teacher=request.user.profile.Teacher).first()
    students_list = [student for student in teacher_group.students.all()]

    if request.method == "POST":
        notice = NoticeForm(request.POST)
        if notice.is_valid():
            object = notice.save(commit=False)
            object.teacher = teacher
            object.save()
            object.students.add(*students_list)
            notice_sent = True
    else:
        notice = NoticeForm()
    return render(request, 'webapp/write_notice.html', {'notice': notice, 'notice_sent': notice_sent})

@login_required
def group_notice(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    return render(request, 'webapp/group_notice_list.html', {'student': student})