from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from ir_project.decorators import admin_access_only
from django.contrib import messages
from ir_project.models import (Region,Topic,UserContact,UserSubcribe,Gallery)
from user.models import CustomUser
from studentTeam.models import StudentProfile,Student
from teacherTeam.models import TeacherProfile,Teacher
from article.models import TopicArticle,Event



# Create your views here.

# Start Topics
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def topic_list(request):
    topics = Topic.objects.all().order_by('name')
    context = {
        'topics':topics
    }
    return render(request,'super-admin/topic/topic-list.html',context)
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def topic_add(request):
    if request.method == 'POST':
        topic_title = request.POST['topic_name']
        topic_img = request.FILES['topic_image']
        topic = Topic.objects.filter(name = topic_title).first()
        if topic is None:
            topic_save = Topic.objects.create(
                name = topic_title,
                image = topic_img
            )
            if topic_save:
                topic_save.save()
                messages.add_message(request,messages.SUCCESS,'New Topic Add Successfully')
                return redirect('sadmin:topic_list')
        else:
            messages.add_message(request,messages.ERROR,'Topic All ready Added')
            return redirect('sadmin:topic_list')
    else:
        messages.add_message(request,messages.ERROR,'Topic All ready Added')
        print('Wrong')
        return redirect('sadmin:topic_list')
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def topic_get(request):
    if request.method == 'POST':
        topic_id = request.POST['topic']
        topic = Topic.objects.filter(id = int(topic_id)).values_list('id','name','image').first()
        return JsonResponse({'status':"Success",'topic':topic},safe=False)
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def topic_edit(request):
    if request.method == 'POST':
        topic_id = request.POST['topic_id']
        topic_title = request.POST['edit_topic_name']
        try:
            topic_image = request.FILES['edit_topic_image']
        except:
            topic_image = ' '
        topic_edit = Topic.objects.get(id = int(topic_id))
        topic_edit.name = topic_title
        if topic_image != ' ':
            topic_edit.image = topic_image
        topic_edit.save()
        messages.add_message(request,messages.SUCCESS,topic_title+" edit Successfully")
        return redirect('sadmin:topic_list')
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def topic_delete(request,topic_slug):
    topic = Topic.objects.filter(slug = topic_slug).delete()
    if topic:
        messages.add_message(request,messages.SUCCESS,'Topic delete Successfully')
        return redirect("sadmin:topic_list")
# End Topics
# Start Region
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def region_list(request):
    regions = Region.objects.all().order_by('name')
    context ={
        'regions':regions
    }
    return render(request,'super-admin/region/region-list.html',context)
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def region_add(request):
    if request.method == 'POST':
        region_title = request.POST['region_name']
        region_img = request.FILES['region_image']
        region = Region.objects.filter(name = region_title).first()
        if region is None:
            region_save = Region.objects.create(
                name = region_title,
                image = region_img
            )
            if region_save:
                region_save.save()
                messages.add_message(request,messages.SUCCESS,'New Region  Add successfully')
                return redirect('sadmin:region_list')
        else:
            messages.add_message(request,messages.ERROR,'Region All ready Added')
            return redirect('sadmin:region_list')
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def region_get(request):
    if request.method == 'POST':
        region_id = request.POST['region']
        region = Region.objects.filter(id = int(region_id)).values_list('id','name','image').first()
        return JsonResponse({'status':"Success",'region':region},safe=False)
    
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def region_edit(request):
    if request.method == 'POST':
        region_id = request.POST['region_id']
        region_title = request.POST['edit_region_name']
        try:
            region_image = request.FILES['edit_region_image']
        except:
            region_image = ' '
        region_edit = Region.objects.get(id = int(region_id))
        region_edit.name = region_title
        if region_image != ' ':
            region_edit.image = region_image
        region_edit.save()
        messages.add_message(request,messages.SUCCESS,region_title+" edit Successfully")
        return redirect('sadmin:region_list')
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def region_delete(request,region_slug):
    delete_region = Region.objects.filter(slug = region_slug).delete()
    if delete_region:
        messages.add_message(request,messages.SUCCESS,'Region Delete Successfully')
        return redirect('sadmin:region_list')
# End Region
# Start Student team
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def student_team_list(request):
    students = StudentProfile.objects.all()
    context = {
        'students':students
    }
    return render(request,'super-admin/student-team/student-team-list.html',context)
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def student_add(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        student_id = request.POST['student_id']
        image = request.FILES['profile_image']
        password = request.POST['password']
        con_password = request.POST['con_password']
        check = 0
        if password != con_password:
            check = 1
            messages.add_message(request,messages.WARNING,'password not match')
        customer = CustomUser.objects.filter(email = email).first()
        if customer is not None:
            check = 1
            messages.add_message(request,messages.WARNING,'Email address all-ready added')
        phone = StudentProfile.objects.filter(phone_number = phone_number).first()
        if phone is not None:
            check = 1
            messages.add_message(request,messages.WARNING,'Phone number all-ready added')
        student = StudentProfile.objects.filter(student_id = student_id).first()
        if student is not None:
            check = 1
            messages.add_message(request,messages.WARNING,'Student id all-ready added')
        if check == 0:
            student_data = Student.objects.create_student(
                user_name =username,
                email = email,
                password = password
            )
            student_data.save()
            student_profile = StudentProfile.objects.filter(user = student_data).first()
            student_profile.phone_number = phone_number
            student_profile.student_id = student_id
            student_profile.image = image
            student_profile.save()
            return redirect('sadmin:student_team_list')

    return render(request,'super-admin/student-team/add.html')
# def student_edit(request):
#     if request.method == 'POST':
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def student_get(request):
    if request.method == 'POST':
        student_id = request.POST['student']
        student = StudentProfile.objects.filter(id = int(student_id)).values_list('id','user__user_name','user__email','student_id', 'phone_number','image').first()
        return JsonResponse({'status':"success",'student':student},safe=False)
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def student_profile_edit(request):
    if request.method == 'POST':
        student_profile_id = request.POST['editstudentid']
        std_profile = StudentProfile.objects.get(id = int(student_profile_id))
        std_id = std_profile.user.id 
        username = request.POST['user_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        student_id = request.POST['student_id']
        email_check = CustomUser.objects.filter(email = email).exclude(id = std_id).first()
        check = 0
        if email_check is not None:
            check = 1
            messages.add_message(request,messages.WARNING,email +' All-ready Added')
        phone_check = StudentProfile.objects.filter(phone_number = phone_number).exclude(id = int(student_profile_id)).first()
        if phone_check is not None:
            check = 1
            messages.add_message(request,messages.WARNING,phone_number +' All-ready Added')
        student_id_check = StudentProfile.objects.filter(student_id = student_id).exclude(id = int(student_profile_id)).first()
        if student_id_check is not None:
            check = 1
            messages.add_message(request,messages.WARNING,student_id +' All-ready Added')
        try:
            image = request.FILES['edit_profile_image']
        except:
            image = " "
        student = StudentProfile.objects.get(id = int(student_profile_id))
        user_id = student.user.id
        student.phone_number = phone_number
        student.student_id = student_id
        if image != ' ':
            student.image = image
        if check == 0:
            CustomUser.objects.filter(id = int(user_id)).update(
                user_name = username,
                email = email
            )
            student.save()
            messages.add_message(request,messages.SUCCESS,username +' Edit Successfully')
        else:
            print('not')
        return redirect('sadmin:student_team_list')
@login_required(login_url='/super-admin/log-in')
@admin_access_only()    
def student_profile_delete(request,user_id):
    CustomUser.objects.filter(id = user_id).delete()
    return redirect('sadmin:student_team_list')
# End Student team
# Start teacher team
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def teacher_team_list(request):
    teachers = TeacherProfile.objects.all()
    context = {
        'teachers':teachers
    }
    return render(request,'super-admin/teacher-team/teacher-team-list.html',context)
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def teacher_add(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        image = request.FILES['profile_image']
        password = request.POST['password']
        con_password = request.POST['con_password']
        check = 0
        if password != con_password:
            check = 1
            messages.add_message(request,messages.WARNING,'password not match')
        customer = CustomUser.objects.filter(email = email).first()
        if customer is not None:
            check = 1
            messages.add_message(request,messages.WARNING,'Email address all-ready added')
        phone = TeacherProfile.objects.filter(phone_number = phone_number).first()
        if phone is not None:
            check = 1
            messages.add_message(request,messages.WARNING,'Phone number all-ready added')
        if check == 0:
            teacher_data = Teacher.objects.create_teacher(
                user_name =username,
                email = email,
                password = password
            )
            teacher_data.save()
            teacher_profile = TeacherProfile.objects.filter(user = teacher_data).first()
            teacher_profile.phone_number = phone_number
            teacher_profile.image = image
            teacher_profile.save()
            return redirect('sadmin:teacher_team_list')
    return render(request,'super-admin/teacher-team/add.html')

@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def teacher_get(request):
    if request.method == 'POST':
        teacher_id = request.POST['teacher']
        teacher = TeacherProfile.objects.filter(id = int(teacher_id)).values_list('id','user__user_name','user__email','phone_number','image').first()
        return JsonResponse({'status':"success",'teacher':teacher},safe=False)

@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def teacher_team_edit(request):
    if request.method == 'POST':
        
        teacher_id = request.POST['editteacherid']
        teacher_profile = TeacherProfile.objects.get(id = int(teacher_id))
        teacher_user_id = teacher_profile.user.id
        
        user_name = request.POST['user_name']
        email = request.POST['email']
        custom_user = CustomUser.objects.filter(email = email).exclude(id = int(teacher_user_id)).first()
        teachercheck = 0
        if custom_user is not None:
            teachercheck = 1
            messages.add_message(request,messages.WARNING,email+" All ready Added")

        phone_number = request.POST['phone_number']
        phone_number_check = TeacherProfile.objects.filter(phone_number = phone_number).exclude(id = int(teacher_id)).first()
        if phone_number_check is not None:
            teachercheck = 1
            messages.add_message(request,messages.WARNING,phone_number+" All ready Added")
        try:
            image = request.FILES['teacher_profile_image']
        except:
            image = " "
        profile = TeacherProfile.objects.get(id = int(teacher_id))
        if image != " ":
            profile.image = image

        if teachercheck == 0:
            profile.phone_number = phone_number
            profile.save()
            CustomUser.objects.filter(id = int(teacher_user_id)).update(
                user_name = user_name,
                email = email
            )
            messages.add_message(request,messages.SUCCESS,user_name+" Edit successfully")
        return redirect('sadmin:teacher_team_list')
@login_required(login_url='/super-admin/log-in')
@admin_access_only()    
def teacher_profile_delete(request,user_id):
    CustomUser.objects.filter(id = user_id).delete()
    return redirect("sadmin:teacher_team_list")
# end teacher team
@login_required(login_url='/super-admin/log-in')
@admin_access_only()
def home(request):
    if request.user.is_authenticated:
        event = Event.objects.count()
        article = TopicArticle.objects.count()
        student = StudentProfile.objects.count()
        teacher = TeacherProfile.objects.count()
        contact = UserContact.objects.count()
        subscribe = UserSubcribe.objects.count()
        context ={
            'event':event,
            'article':article,
            'student':student,
            'teacher':teacher,
            'contact':contact,
            'subscribe':subscribe
        }
        return render(request,'super-admin/home.html',context)
    else:
        return render(request,'super-admin/login.html')

def samdinlogin(request):
    return render(request,'super-admin/login.html')
    
def authenticate_check(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            if request.user.role == "ADMIN":
                messages.add_message(request,messages.SUCCESS,'Login Successfully')
                return redirect('sadmin:home')
            else:
                messages.add_message(request,messages.ERROR,'Sorry! try again')
                return redirect('sadmin:samdinlogin')
        else:
            messages.add_message(request,messages.ERROR,'Sorry! try again')
            return redirect('sadmin:samdinlogin')
    else:
        messages.add_message(request,messages.ERROR,'Sorry! try again')
        return redirect('sadmin:samdinlogin')
def sadminlogout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'Log-out Successfully')
    return redirect('sadmin:home')


def user_contact_list(request):
    contact_data = UserContact.objects.all().order_by('-id')
    context = {
        'contact_data':contact_data
    }
    return render(request,'super-admin/user-contact-list.html',context)

def user_subscribe_list(request):
    subscribe_data = UserSubcribe.objects.all().order_by('-id')
    context = {
        'subscribe_data':subscribe_data
    }
    return render(request,'super-admin/subscribe-list.html',context)

def gallery_photo(request):
    photos = Gallery.objects.all().order_by('-id')
    context = {
        'photos':photos
    }
    return render(request,'super-admin/archive/gallery-photo.html',context)

def gallery_photo_save(request):
    if request.method == 'POST':
        image = request.FILES['upload_image']

        photo_save = Gallery.objects.create(
            image = image
        )
        if photo_save:
            photo_save.save()
            messages.add_message(request,messages.SUCCESS,'Gallery Photo add successfully')

    return redirect("sadmin:gallery_photo")