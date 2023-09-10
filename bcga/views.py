from django.shortcuts import render
from ir_project.models import (Topic,Region,Interview,Podcast)
# Create your views here.
def home(request):
    context={
        'page_info':''
    }
    return render(request,'bcga/home.html',context)

def topic(request,topic):
    page_info = Topic.objects.get(slug = topic)
    context={
        'page_info':page_info
    }
    return render(request,'bcga/topic.html',context)

def about_us(request):
    return render(request,'bcga/about-us.html')

def contact_us(request):
    return render(request,'bcga/contact-us.html')

def interview(request,interview):
    return render(request,'bcga/interview.html')

def new_event(request):
    return render(request,'bcga/event.html')

def post_event(request):
    return render(request,'bcga/past-event.html')

def podcast(request,podcast):
    return render(request,'bcga/podcast.html')

def student_team(request):
    return render(request,'bcga/student-team.html')

def teacher_team(request):
    return render(request,'bcga/teacher-team.html')
def region_topic(request,topic):
    return render(request,'bcga/region-topic.html')