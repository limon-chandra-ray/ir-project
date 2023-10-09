from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from article.models import TopicArticle,TopicError
from user.models import CustomUser
from ir_project.decorators import teacher_access_only
# Create your views here.
def login_view(request):
    return render(request,'teachert/login.html')

def auth_check(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        student_check = authenticate(request,username = email,password = password)
        if student_check is not None:
            login(request,student_check)
            if request.user.role == 'TEACHER':
                messages.add_message(request,messages.SUCCESS,'Login Successfully')
                return redirect('teacherTeam:home')
            else:
                logout(request) 
                messages.add_message(request,messages.ERROR,'You are invalid student ')
                return redirect('teacherTeam:login_view')   
        else:
            messages.add_message(request,messages.ERROR,'You are invalid student ')
            return redirect('teacherTeam:login_view')
def teacher_logout(request):
    logout(request)
    return redirect('teacherTeam:home')

@login_required(login_url='/teacher/log-in')
@teacher_access_only()
def home(request):
    return render(request,'teachert/home.html')


def article_show(request):
    articles = TopicArticle.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'teachert/article-list.html',context)

def article_details(request,article_slug):
    article = TopicArticle.objects.get(slug =article_slug)
    context = {
        'article':article
    }
    return render(request,'teachert/article-details.html',context)

def error_describe_save(request):
    if request.method == 'POST':
        article_id = request.POST['article_id']
        error_comment = request.POST['errorComment']
        save_error_comment = TopicError.objects.create(
            topic = TopicArticle.objects.get(id = int(article_id)),
            tacher = request.user,
            error_text = error_comment
        )
        if save_error_comment:
            messages.add_message(request,messages.SUCCESS,'Comment Create Successfully')
        else:
            messages.add_message(request,messages.ERROR,'Comment not Created')
    else:
        messages.add_message(request,messages.ERROR,'Comment Create time some error data add')
    return redirect("teacherTeam:article_show")

def article_accepted(request,article_id):
    update_article_status = TopicArticle.objects.filter(id = article_id).update(
        status = 1
    )
    if update_article_status:
        messages.add_message(request,messages.SUCCESS,'Article Accept Successfully')
        return redirect('teacherTeam:article_show')
    

def event_show(request):
    return render(request,'teachert/event-list.html')