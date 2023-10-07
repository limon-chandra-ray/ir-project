from functools import wraps
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
def student_test_func(user):
    if user.role == 'STUDENT':
        return True
    return False

def student_access_only(view_to_return = 'studentTeam:login_view'):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request,*args, **kwargs):
            if not student_test_func(request.user):
                logout(request)
                messages.add_message(request,messages.WARNING,'Try again')
                return  redirect(view_to_return)
            return view(request,*args, **kwargs)
        return _wrapped_view
    return decorator

def teacher_test_func(user):
    if user.role == 'TEACHER':
        return True
    return False

def teacher_access_only(view_to_return = 'teacherTeam:login_view'):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request,*args, **kwargs):
            if not teacher_test_func(request.user):
                logout(request)
                messages.add_message(request,messages.WARNING,'Try again')
                return  redirect(view_to_return)
            return view(request,*args, **kwargs)
        return _wrapped_view
    return decorator
def admin_test_func(user):
    if user.role == 'ADMIN':
        return True
    return False

def admin_access_only(view_to_return = 'sadmin:samdinlogin'):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request,*args, **kwargs):
            if not admin_test_func(request.user):
                logout(request)
                messages.add_message(request,messages.WARNING,'Try again')
                return  redirect(view_to_return)
            return view(request,*args, **kwargs)
        return _wrapped_view
    return decorator
