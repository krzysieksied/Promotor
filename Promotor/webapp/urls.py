from django.urls import path

from . import views

app_name = 'webapp'



urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name="student_detail"),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name="teacher_detail"),
    path('teacher/group_students_list', views.group_students_list, name="group_student_list"),
]
