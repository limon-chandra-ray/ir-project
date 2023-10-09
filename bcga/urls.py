from django.urls import path
app_name = 'bcga'
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('subscribe-page',views.subscribe_webpage,name='subscribe_webpage'),
    path('topic-<slug:topic>',views.topic,name='topic'),
    path('region-topic-<slug:topic>',views.region_topic,name='region_topic'),
    path('<slug:topic_article>-topic-deaitls',views.article_detial,name='article_detial'),
    path('about-us',views.about_us,name='about_us'),
    path('student-team',views.student_team,name='student_team'),
    path('teacher-team',views.teacher_team,name='teacher_team'),
    path('archive',views.archive_view,name='archive_view'),
    path('contact-us',views.contact_us,name='contact_us'),
    path('contact-save',views.contact_save,name='contact_save'),
    path('interview-<slug:interview>',views.interview,name='interview'),
    path('new-events',views.new_event,name='new_event'),
    path('event-<slug:event_slug>',views.event_detail,name='event_detail'),
    path('participate-save',views.event_participator_save,name='event_participator_save'),
    path('past-event',views.past_event,name='past_event'),
    path('podcast-<slug:podcast>',views.podcast,name='podcast'),
    path('articel-comment',views.article_comment_save,name='article_comment_save')
    
]
