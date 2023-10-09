from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from studentTeam.forms import StudentTeamForm
from ir_project.models import Topic,Region
from .models import StudentProfile
from article.models import TopicArticle,Event,EventParticipate
from ir_project.decorators import student_access_only
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
# Create your views here.
def login_view(request):
    return render(request,'studentt/login.html')
def auth_check(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        student_check = authenticate(request,username = email,password = password)
        if student_check is not None:
            login(request,student_check)
            if request.user.role == 'STUDENT':
                print('success')
                messages.add_message(request,messages.SUCCESS,'Login Successfully')
                return redirect('studentTeam:home')
            else:
                logout(request) 
                print('Logout')
                messages.add_message(request,messages.ERROR,'You are invalid student ')
                return redirect('studentTeam:login_view')   
        else:
            print('not user')
            messages.add_message(request,messages.ERROR,'You are invalid student ')
            return redirect('studentTeam:login_view')
def student_logout(request):
    logout(request)
    return redirect('studentTeam:home')


@login_required(login_url='/student/log-in')
@student_access_only()
def home(request):
    student =StudentProfile.objects.get(user = request.user)
    total_event = Event.objects.count()
    total_article = TopicArticle.objects.count()
    context ={
        "student":student,
        'total_article':total_article,
        'total_event':total_event
        }
    return render(request,'studentt/home.html',context)

@login_required(login_url='/student/log-in')
@student_access_only()
def article_view(request):
    articles = TopicArticle.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'studentt/articles.html',context)
@login_required(login_url='/student/log-in')
@student_access_only()
def create_article_view(request):
    topics = Topic.objects.exclude(name = 'All Articles')
    regions = Region.objects.all().order_by('name')

    context = {
        'topics':topics,
        'regions':regions
    }
    return render(request,'studentt/create-article.html',context)
@login_required(login_url='/student/log-in')
@student_access_only()
def create_article_save(request):
    title = request.POST['title']
    topic = request.POST['topic_id']
    image = request.FILES['image']
    region = request.POST['region_id']
    article_content = request.POST['article_content'] 
    topic_article = TopicArticle.objects.create(
        topic = Topic.objects.get(id = int(topic)),
        title = title,
        image = image,
        region = Region.objects.get(id = int(region)),
        artice_content = article_content
    )
    topic_article.save()

    return redirect('studentTeam:home')
@login_required(login_url='/student/log-in')
@student_access_only()
def articleDetail(request,articleSlug):
    article = TopicArticle.objects.get(slug = articleSlug)
    context = {
        'article':article
    }
    return render(request,'studentt/article-details.html',context)
@login_required(login_url='/student/log-in')
@student_access_only()
def articleEdit(request,articleSlug):
    article = TopicArticle.objects.get(slug=articleSlug)
    topics = Topic.objects.all().order_by('name')
    if request.method == 'POST':
        title = request.POST['title']
        topic = request.POST['topic_id']
        try:
            image = request.FILES['image']
        except:
            image = ' '
        article_content = request.POST['article_content'] 
        topic_article = TopicArticle.objects.get(slug =articleSlug)
        topic_article.topic = Topic.objects.get(id = int(topic))
        topic_article.title = title
        topic_article.artice_content = article_content
        if image !=' ':
            topic_article.image = image
        if topic_article:
            topic_article.save()
            return redirect('studentTeam:article_view')
    else:
        context = {
            'article':article,
            'topics':topics
        }
        return render(request,'studentt/article-edit.html',context)
@login_required(login_url='/student/log-in')
@student_access_only()
def articleDelete(request,articleSlug):
    article = TopicArticle.objects.filter(slug = articleSlug).delete()
    if article:
        return redirect('studentTeam:article_view')
# event 
@login_required(login_url='/student/log-in')
@student_access_only()
def event_list(request):
    events = Event.objects.all().order_by('-id')
    context = {
        'events':events
    }
    return render(request,'studentt/event-list.html',context)
@login_required(login_url='/student/log-in')
@student_access_only()
def event_create_view(request):
    return render(request,'studentt/create-event.html')
@login_required(login_url='/student/log-in')
@student_access_only()
def event_create_save(request):
    if request.method == 'POST':
        title = request.POST['title']
        cheaf_guest = request.POST['cheaf_guest']
        image = request.FILES['image']
        event_date = request.POST['event_date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        event_content = request.POST['event_content']
        cheafGuest_content = request.POST['cheafGuest_content']

        event_save = Event.objects.create(
            title = title,
            cheaf_guest = cheaf_guest,
            guest_details_info = cheafGuest_content,
            event_content = event_content,
            event_date = event_date,
            event_start = start_time,
            event_end = end_time,
            image = image
        )
        event_save.save()
        return redirect("studentTeam:event_list")
@login_required(login_url='/student/log-in')
@student_access_only()
def eventDetail(request,eventSlug):
    event = Event.objects.get(slug = eventSlug)
    context = {
        'event':event
    }
    return render(request,'studentt/event-details.html',context)
@login_required(login_url='/student/log-in')
@student_access_only()
def eventEdit(request,eventSlug):
    event = Event.objects.get(slug = eventSlug)
    if request.method == 'POST':
        title = request.POST['title']
        cheaf_guest = request.POST['cheaf_guest']
        event_date = request.POST['event_date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        event_content = request.POST['event_content']
        cheafGuest_content = request.POST['cheafGuest_content']
        event.event_date = datetime.strptime(event_date,'%Y/%m/%d')
        event.save()
        return redirect('studentTeam:event_list')



    context ={
        'event':event
    }
    return render(request,'studentt/event-edit.html',context)
@login_required(login_url='/student/log-in')
@student_access_only()
def eventDelete(request,eventSlug):
    event_delete = Event.objects.filter(slug = eventSlug).delete()
    if event_delete:
        return redirect('studentTeam:event_list')
    
@login_required(login_url='/student/log-in')
@student_access_only()
def event_participator_list(request,event_id):
    event = Event.objects.get(id = event_id)
    event_participates = EventParticipate.objects.filter(event = event).order_by('full_name')
    context = {
        'event_participates': event_participates
    }
    return render(request,'studentt/event-participate-list.html',context)