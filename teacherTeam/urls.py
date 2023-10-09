from django.urls import path
from . import views
app_name = 'teacherTeam'
urlpatterns = [
    path('dash-board',views.home,name='home'),
    path('log-in',views.login_view,name='login_view'),
    path('auth-check',views.auth_check,name='auth_check'),
    path('teacher-log-out',views.teacher_logout,name='teacher_logout'),
    path('article-list',views.article_show,name='article_show'),
    path('article-details-<slug:article_slug>',views.article_details,name='article_details'),
    path('article-error-comment-save',views.error_describe_save,name='error_describe_save'),
    path('article-accepted-<int:article_id>',views.article_accepted,name='article_accepted'),
    path('event-list',views.event_show,name='event_show'),
]
