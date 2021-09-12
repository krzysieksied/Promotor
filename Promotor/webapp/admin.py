from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Student, Teacher, Group, StudentMessage, ProfilUser, ThreadModel


# Register your models here.


class StudentMessageInlineAdmin(admin.TabularInline):
    model = StudentMessage


class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentMessageInlineAdmin]


class ProfilUserAdmin(admin.ModelAdmin):
    pass


class StudentInlineAdmin(admin.TabularInline):
    model = Student





class TeacherAdmin(admin.ModelAdmin):
    inlines = [StudentMessageInlineAdmin]


class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInlineAdmin]


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ProfilUser,ProfilUserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(ThreadModel)