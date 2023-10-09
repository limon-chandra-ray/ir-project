from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse
from ir_project.models import (Topic,Region,
                               Interview,
                               Podcast,UserContact,
                               UserSubcribe,
                               Gallery
                               )
from article.models import (TopicArticle,
                            Event,
                            Comment,
                            Department,
                            StudentSession,
                            EventParticipate
                            )
from studentTeam.models import StudentProfile
from teacherTeam.models import TeacherProfile
from datetime import datetime,date
from django.contrib import messages

# Create your views here.
def home(request):
    latest_article1 = TopicArticle.objects.all().order_by('-id')[:3]
    latest_article2 = TopicArticle.objects.all().order_by('-id')[3:6]
    latest_event = Event.objects.all().order_by('-id')[:3]
    context={
        'page_info':'',
        'latest_article':latest_article1,
        'latest_article2':latest_article2,
        'latest_event':latest_event
    }
    return render(request,'bcga/home.html',context)

def topic(request,topic):
    page_info = Topic.objects.get(slug = topic)
    if topic == 'all-articles':
        topic_articles = TopicArticle.objects.all().order_by('-id')[:10]
        context={
        'page_info':page_info,
            'topic_articles':topic_articles
        }
        return render(request,'bcga/all-topic.html',context)
    else:
        topic_articles = TopicArticle.objects.filter(topic = page_info).order_by('-id')
        all_topic = Topic.objects.all().order_by('name')
        context={
            'page_info':page_info,
            'topic_articles':topic_articles,
            'all_topics':all_topic
        }
        return render(request,'bcga/topic.html',context)

def article_detial(request,topic_article):
    article = TopicArticle.objects.get(slug = topic_article)
    comment = article.comment_set.all()
    context ={
        'article':article,
        'comments':comment
    }
    return render(request,'bcga/article_details.html',context)

def about_us(request):
    return render(request,'bcga/about-us.html')

def contact_us(request):
    return render(request,'bcga/contact-us.html')
def contact_save(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_save = UserContact.objects.create(
            first_name =f_name,
            last_name = l_name,
            email = email,
            contact_sub = subject,
            contact_message = message
        )
        if contact_save:
            messages.add_message(request,messages.SUCCESS,'Your Contact added successfully')
            return redirect('bcga:home')
        
        else:
            messages.add_message(request,messages.SUCCESS,'Your Contact not added')
            context = {
                'first_name' :f_name,
                'last_name' : l_name,
                'email' : email,
                'contact_sub' : subject,
                'contact_message' : message
            }
        return render(request,'bcga/contact-us.html',context)
def interview(request,interview):
    return render(request,'bcga/interview.html')

def new_event(request):
    events = Event.objects.filter(event_date__gte = date.today()).order_by('id')[:]
    context = {
        'events':events
    }
    return render(request,'bcga/event.html',context)
def event_detail(request,event_slug):
    event = Event.objects.get(slug = event_slug)
    depts = Department.objects.all().order_by('name')
    sessions = StudentSession.objects.all().order_by('-name')
    context={
        'event':event,
        'depts':depts,
        'sessions':sessions
    }
    return render(request,'bcga/event-details.html',context)

def event_participator_save(request):
    if request.method == 'POST':
        event_id = request.POST['event_id']
        user_name = request.POST['user_name']
        phone_number = request.POST['phone_number']
        std_year = request.POST['std_year']
        std_dept = request.POST['std_dept']
        std_session = request.POST['std_session']
        student_id = request.POST['student_id']
        event = Event.objects.get(id = int(event_id))
        check_event = EventParticipate.objects.filter(event = event,student_id = student_id).first()
        if check_event is None:
            registration_save = EventParticipate.objects.create(
                event = event,
                full_name = user_name,
                student_id = student_id,
                phone_number = phone_number,
                student_dept = Department.objects.get(id = int(std_dept)),
                student_year = std_year ,
                student_session =StudentSession.objects.get(id = int(std_session))
            )
            if registration_save:
                messages.add_message(request,messages.SUCCESS,'Your Registration Successfully')
        else:
            messages.add_message(request,messages.WARNING,'Your Registration all-ready Successfully')
        return redirect('bcga:event_detail',event_slug=event.slug)

def past_event(request):
    past_event = Event.objects.filter(created_at__lt = datetime.today())
    context = {
        'past_events':past_event
    }
    return render(request,'bcga/past-event.html',context)

def podcast(request,podcast):
    return render(request,'bcga/podcast.html')

def region_topic(request,topic):
    page_info = Region.objects.get(slug = topic)
    region = Region.objects.all().order_by('name')
    topic_articles = TopicArticle.objects.filter(region = page_info).order_by('-id')
    context={
        'page_info':page_info,
        'topic_articles':topic_articles,
        'regions':region
    }
    return render(request,'bcga/region-topic.html',context)

def subscribe_webpage(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        check_email = UserSubcribe.objects.filter(email = email).first()
        if check_email is None:
            subscribe_save = UserSubcribe.objects.create(
                first_name =f_name,
                last_name = l_name,
                email = email
            )
            if subscribe_save:
                messages.add_message(request,messages.SUCCESS,'Your Subscription Successfully')
        else:
            messages.add_message(request,messages.SUCCESS,'Your Subscription all-ready Successfully')
    return redirect("bcga:home")

def article_comment_save(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        comment_text = request.POST['comment_text']
        article_id = request.POST['article_id']
        article = TopicArticle.objects.get(id = int(article_id))
        check = Comment.objects.filter(article = article,user_name=user_name).first()
        if check is None:
            article_comment_save = Comment.objects.create(
                user_name = user_name,
                comment_text = comment_text,
                article = article
            )
            if article_comment_save:
                messages.add_message(request,messages.SUCCESS,'Comment Successfully')
                status = {"status":"Success"}
        else:
            status = {"status":"Error"}
    else:
        status = {"status":"Error"}
    return JsonResponse(status)

def student_team(request):
    students = StudentProfile.objects.all().order_by("-id")
    context = {
        'students':students
    }
    return render(request,'bcga/student-team.html',context)

def teacher_team(request):
    teachers = TeacherProfile.objects.all().order_by("-id")
    context = {
        'teachers':teachers
    }
    return render(request,'bcga/teacher-team.html',context)
def archive_view(request):
    gallery_photos = Gallery.objects.all().order_by('-id')[:9]
    context = {
        'gallery_photos':gallery_photos
    }
    return render(request,'bcga/archive.html',context)


# Error 404 and 500 Handler 
def error_404_view(request,exception):
    return render(request,'notifications/error_404.html')
def error_500_view(request):
    return render(request,'notifications/error_500.html')