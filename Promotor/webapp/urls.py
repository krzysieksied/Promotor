from django.urls import path

from . import views
from .views import ListThreads, CreateThread, ThreadView, CreateMessage

app_name = 'webapp'



urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name="student_detail"),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name="teacher_detail"),
    path('teacher/group_students_list', views.group_students_list, name="group_student_list"),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
    path('inbox/<int:pk>/sm/', views.StudentMessage, name='student_message'),
    path('teacher/write_notice',views.add_notice,name="write_notice"),
    path('student/<int:pk>/group_notice',views.group_notice,name="group_notice"),
]
