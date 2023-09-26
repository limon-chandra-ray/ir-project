from django.urls import path
app_name = 'studentTeam'
from . import views
urlpatterns = [
    path('',views.home,name='home')
]

