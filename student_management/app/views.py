import random
import string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from app.models import LoginForm, PasswordResetCode, Course
from django.contrib.auth import logout, authenticate, login
from .forms import SignUpForm, ResetPasswordForm, EnrollmentForm, AddCourseForm, EditCourseForm
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    error_message = ''
    successful = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            # """
            # user = User(
            #     username=form.cleaned_data['username'],
            #     password=form.cleaned_data['password'],
            #     email=form.cleaned_data['email'],
            # )
            # """
            # save the user to the database
            # print(user.username)
            # print(user.password)
            # print(user.email)
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.add_message(request, messages.ERROR, 'User already exists, please try again.')
        
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'])
            user.save()
            successful = 'Your account was created successfully.'
            request.session['user_id'] = user.id
            # redirect to the home page
            return redirect('login')
        else:
            error_message = 'Invalid register. Please try again'
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message, 'successful':successful})
    
def home(request):
    return render(request, 'home.html')

def logout(request):
    logout(request)
    return redirect('login')

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            # generate a random password reset code (.32lekal;wke)
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            # send an email to the user's email address with the password reset code
            send_mail(
                'Password reset code',
                f'Your password reset code is: {code}',
                'your_email@example.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            # To save the password reset code and the user's email address in the database
            PasswordResetCode.objects.create(
                code=code,
                email=form.cleaned_data['email'],
            )
            # redirect the user to the password reset page ..2 x 3 
            return redirect('password_reset_code')
    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})

def display_catalog(request):
    courses = Course.objects.filter('')
    context = {'courses':courses}
    return render(request, 'catalog.html', context)

def enroll(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            course = Course.object.get(course_code = form.cleaned_data['course_code'])
            if form.cleaned_data['meet_requirements']:
                course.enrollment += 1
                course.save()
                message.success(request, 'Enrollment successful.')
            else:
                message.error(request," You do not have enough requirements to enroll this course")
            return redirect('catalog')
    else:
        form = EnrollmentForm()
    return render(request, 'enroll.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'New course added')
            return redirect('catalog')
    else:
        form = AddCourseForm()
    return render(request, 'add_course.html', {'form': form, 'course':course})

def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method =='POST':
        form = EditCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, " course has been updated successful")
            return redirect('catalog')
    else:
        form = EditCourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})

def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.delete()
    messages.success(request, 'Course has been deleted')
    return redirect('catalog')