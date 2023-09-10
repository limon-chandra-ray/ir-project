from django.urls import path
app_name = 'ir_project'
from . import views
urlpatterns = [
    path('topic',views.topic_get,name='topic_get'),
    path('region',views.region_get,name='region_get'),
    path('podcast',views.podcast_get,name='podcast_get'),
    path('interview',views.interview_get,name='interview_get'),

]
