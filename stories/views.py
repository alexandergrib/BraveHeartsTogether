from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from accounts.models import Profile
from stories.forms import StoryForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from braveheartstogether import settings
from stories.models import Story


def stories(request):
    """Display all stories from database"""
    all_stories = list(Story.objects.all())
    context = {
        'stories': all_stories
    }
    template = 'stories/story.html'
    return render(request, template, context)


def add_story(request):
    """Add new user story"""

    # if not request.user.is_superuser:
    #     raise PermissionDenied()
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            images = request.FILES.getlist('image')
            user.username = User.objects.get(username=request.user)
            user.save()
            messages.success(request, f'Successfully added "{user.title}"')
            return redirect('add_story')
        else:
            messages.error(
                request,
                'Something went wrong please try again')
    else:
        form = StoryForm()

    template = 'stories/story.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    form = StoryForm(instance=story)
    template = 'stories/edit_story.html'
    context = {
        'form': form,
        'story': story
    }
    return render(request, template, context)


def delete_story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    story.delete()
    return redirect(reverse('stories'))
