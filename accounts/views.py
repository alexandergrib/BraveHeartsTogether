from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterUserForm, ProfileForm
from accounts.models import Profile


# login / logout / user registration system
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,
                             "There was an error logging in, please try again")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('home')

# TODO: create profile on user creation
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful!")
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
    # user = User.objects.filter(user=request.user)
    context = {
        # 'user': user
    }
    return render(request, 'accounts/account.html', context)
