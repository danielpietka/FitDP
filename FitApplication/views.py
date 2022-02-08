from ast import Try
from django.db import IntegrityError
from django.shortcuts import redirect, render
from FitApplication.forms import UserForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'diet/signupuser.html' , {'form':UserForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'], email = request.POST['email'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'diet/signupuser.html' , {'form':UserForm(), 'error':"That username has already been taken. Choose a new one"})
        else:
            return render(request, 'diet/signupuser.html', {'form':UserForm(), 'error':'Passwords did not match'})
