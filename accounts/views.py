from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterUserForm, ProfileForm
from .models import Profile
from django.views.generic import ListView
from django.views import generic


def notRegistered(request):
    return render(request, "notRegistered.html", {})


# login / logout / user registration system
def login_user(request, username, password):
    if request.method == 'POST':
        # Get the username and password from the request
        username = request.POST['username']
        password = request.POST['password']
        # Call the login_user function with the request, username, and password
        login_user(request, username, password)
        if request.user.is_authenticated:
            user = authenticate(request, username=username, password=password)
            user_id = request.user.id
            login(request, user)
            return redirect('account')
        else:
            return redirect('login')
    else:
        return redirect('login')

    return render(request, 'accounts/login.html', {})

    print(user)


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
            return redirect('account')
    else:
        form = RegisterUserForm()
    return render(request, 'accounts/register_user.html', {'form': form, })


# form inputs
def First_name(request):
    if request.method == "POST":
        First_name = request.POST["First_name"]


def Last_name(request):
    if request.method == "POST":
        Last_name = request.POST["Last_name"]


def Email(request):
    if request.method == "POST":
        Email = request.POST["Email"]


def account(request):
    profiles = Profile.objects.filter(user=request.user)
    context = {
        'user': profiles
    }
    return render(request, 'accounts/account.html', context)



def profileEdit(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts/account.html')
    form = ProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profileEdit.html', context)


def profileDelete(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    profile.delete()
    return redirect('accounts/account')


def profile(request):
    profiles = Profile.objects.filter(user=request.user)
    context = {
        'user': profiles
    }
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        Email = request.POST.get('Email')
        About = request.POST.get('About')

        # Store day and service in django session:
        request.session['First_name'] = First_name
        request.session['Last_name'] = Last_name
        request.session['Email'] = Email
        request.session['About'] = About

        if Profile.objects.filter(user=request.user):
            ProfileForm = Profile.objects.get_or_create(
                First_name=First_name,
                Last_name=Last_name,
                Email=Email,
                About=About,
                user=request.user,
            )
            messages.success(request, "Profile Created!")
            return redirect('accounts/account.html')
        else:
            messages.success(request, "The profile was not created!")
    return render(request, 'accounts/account.html', context)

