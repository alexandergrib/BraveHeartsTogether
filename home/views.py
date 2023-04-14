from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from accounts.forms import RegisterUserForm, ProfileForm
from accounts.models import Profile
from stories import views
from django.urls import path
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import *
from . import views
from django.views.generic import ListView
from django.views import generic


def home(request):
    return render(request, "home.html", {})


def blog(request):
    return render(request, "blog.html", {})


def about(request):
    return render(request, "about.html", {})


def account(request):
    return render(request, "account.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, please try again")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('login')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Resigstration successful!"))
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html', {'form': form, })