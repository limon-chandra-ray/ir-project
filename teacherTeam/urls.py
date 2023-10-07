from django.urls import path
from . import views
app_name = 'teacherTeam'
urlpatterns = [
    path('dash-board',views.home,name='home'),
    path('log-in',views.login_view,name='login_view'),
    path('auth-check',views.auth_check,name='auth_check'),
    path('teacher-log-out',views.teacher_logout,name='teacher_logout'),
]
