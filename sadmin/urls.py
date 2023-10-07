from django.urls import path
from . import views
app_name = "sadmin"
urlpatterns = [
    path('',views.home,name='home'),
    path('log-in',views.samdinlogin,name='samdinlogin'),
    path('log-in-check',views.authenticate_check,name='authenticate_check'),
    path('log-out',views.sadminlogout,name='sadminlogout'),
    # start topic path
    path('topic-list',views.topic_list,name='topic_list'),
    path('topic-add',views.topic_add,name='topic_add'),
    path('topic-get',views.topic_get,name='topic_get'),
    path('topic-edit',views.topic_edit,name='topic_edit'),
    path('topic-delete/<slug:topic_slug>',views.topic_delete,name='topic_delete'),
    # end topic path
    # start region path
    path('region-list',views.region_list,name='region_list'),
    path('region-add',views.region_add,name='region_add'),
    path('region-get',views.region_get,name='region_get'),
    path('region-edit',views.region_edit,name='region_edit'),
    path('region-delete/<slug:region_slug>',views.region_delete,name='region_delete'),
    # end region path
    # start student team
    path('student-team-list',views.student_team_list,name='student_team_list'),
    path('student-add',views.student_add,name='student_add'),
    path('student-get',views.student_get,name='student_get'),
    path('student-profile-edit',views.student_profile_edit,name='student_profile_edit'),
    path('student-profile-delete-<int:user_id>',views.student_profile_delete,name='student_profile_delete'),
    # end student team
    # start teacher team
    path('teacher-team-list',views.teacher_team_list,name='teacher_team_list'),
    path('teacher-add',views.teacher_add,name='teacher_add'),
    path('teacher-get',views.teacher_get,name='teacher_get'),
    path('teacher-team-edit',views.teacher_team_edit,name='teacher_team_edit'),
    path('teacher-profile-delete-<int:user_id>',views.teacher_profile_delete,name='teacher_profile_delete'),
    # end teacher team
    path('contact-list',views.user_contact_list,name='user_contact_list'),
    path('subscribe-list',views.user_subscribe_list,name='user_subscribe_list'),
    path('gallery-photo',views.gallery_photo,name='gallery_photo'),
    path('gallery-photo-save',views.gallery_photo_save,name='gallery_photo_save')
]

