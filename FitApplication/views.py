from ast import Try
from django.db import IntegrityError
from django.shortcuts import redirect, render
from FitApplication.forms import UserForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Food

def home(request):
    if request.user.is_authenticated:
        return redirect('signedin')
    else:
        return render(request, 'home.html')

@login_required
def signedin(request):
    return render(request, 'signedin.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == "GET":
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username = request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('signedin')
    

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html' , {'form':UserForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'], email = request.POST['email'])
                user.save()
                login(request, user)
                return redirect('signedin')
            except IntegrityError:
                return render(request, 'signupuser.html' , {'form':UserForm(), 'error':"That username has already been taken. Choose a new one"})
        else:
            return render(request, 'signupuser.html', {'form':UserForm(), 'error':'Passwords did not match'})

def dietuser(request):
    foods = Food.objects.all
    userFood = Food.objects.filter(user = request.user)
    return render(request, 'diet/dietuser.html', {"foods":foods, "userFood":userFood})