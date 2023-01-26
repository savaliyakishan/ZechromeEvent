from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'login.html')


def admin_login(request):
    if request.method == "POST":
        usernmae = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=usernmae, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('Dashboard-Home')
        else:
            messages.error(request, "Login Fail!")
            return render(request, 'login.html')
    return redirect('Index')


def user_logout(request):
    logout(request)
    return redirect('/login/')
