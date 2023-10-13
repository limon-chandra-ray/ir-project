from django.urls import path
app_name = 'studentTeam'
from . import views
urlpatterns = [
    path('log-in',views.login_view,name='login_view'),
    path('auth-check',views.auth_check,name='auth_check'),
    path('student-log-out',views.student_logout,name='student_logout'),
    path('dash-board',views.home,name='home'),
    # start Articles
    path('article-list',views.article_view,name='article_view'),
    path('create-article',views.create_article_view,name='create_article_view'),
    path('save-create-article',views.create_article_save,name='create_article_save'),
    path('article-details-<slug:articleSlug>',views.articleDetail,name='articleDetail'),
    path('article-edit-<slug:articleSlug>',views.articleEdit,name='articleEdit'),
    path('article-delete-<slug:articleSlug>',views.articleDelete,name='articleDelete'),
    # end Articles
    # start Event
    path('event-list',views.event_list,name='event_list'),
    path('event-create',views.event_create_view,name='event_create_view'),
    path('event-create-save',views.event_create_save,name="event_create_save"),
    path('event-details-<slug:eventSlug>',views.eventDetail,name='eventDetail'),
    path('event-edit-<slug:eventSlug>',views.eventEdit,name='eventEdit'),
    path('event-delete-<slug:eventSlug>',views.eventDelete,name='eventDelete'),
    path('event-participate-<int:event_id>',views.event_participator_list,name='event_participator_list')
    # end Event
]

