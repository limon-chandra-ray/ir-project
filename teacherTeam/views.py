from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
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
                print('success')
                messages.add_message(request,messages.SUCCESS,'Login Successfully')
                return redirect('teacherTeam:home')
            else:
                logout(request) 
                print('Logout')
                messages.add_message(request,messages.ERROR,'You are invalid student ')
                return redirect('teacherTeam:login_view')   
        else:
            print('not user')
            messages.add_message(request,messages.ERROR,'You are invalid student ')
            return redirect('teacherTeam:login_view')
def teacher_logout(request):
    logout(request)
    return redirect('teacherTeam:home')

@login_required(login_url='/teacher/log-in')
@teacher_access_only()
def home(request):
    return render(request,'teachert/home.html')