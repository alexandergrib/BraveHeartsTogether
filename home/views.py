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
from stories.models import Story
import random


def home(request):
    all_stories = list(Story.objects.all())
    number = random.randint(0, len(all_stories))
    story = Story.objects.get(pk=number)
    print(story)
    context = {
        'story': story
    }
    return render(request, "home.html", context)


def blog(request):
    return render(request, "blog.html", {})


def about(request):
    return render(request, "about.html", {})



