from django.urls import path
app_name = 'bcga'
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('topic-<slug:topic>',views.topic,name='topic'),
    path('region-topic-<slug:topic>',views.region_topic,name='region_topic'),
    path('about-us',views.about_us,name='about_us'),
    path('contact-us',views.contact_us,name='contact_us'),
    path('interview-<slug:interview>',views.interview,name='interview'),
    path('new-events',views.new_event,name='new_event'),
    path('post-event',views.post_event,name='post_event'),
    path('podcast-<slug:podcast>',views.podcast,name='podcast'),
    path('student-team',views.student_team,name='student_team'),
    path('teacher-team',views.teacher_team,name='teacher_team'),
]
