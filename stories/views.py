from django.contrib.auth.decorators import login_required
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
from django.shortcuts import get_object_or_404, redirect


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


def like_post(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.user in story.likes.all():
        # User already liked the post, remove like
        story.likes.remove(request.user)
    else:
        # User hasn't liked the post yet, add like
        story.likes.add(request.user)
        # Also remove the user from dislikes if they previously disliked the post
        if request.user in story.dislikes.all():
            story.dislikes.remove(request.user)
    return redirect('stories')


def dislike_post(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.user in story.dislikes.all():
        # User already disliked the post, remove dislike
        story.dislikes.remove(request.user)
    else:
        # User hasn't disliked the post yet, add dislike
        story.dislikes.add(request.user)
        # Also remove the user from likes if they previously liked the post
        if request.user in story.likes.all():
            story.likes.remove(request.user)

    return redirect('stories')


def post_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    context = {
        'story': story,
        'like_count': story.likes.count(),
        'dislike_count': story.dislikes.count()
    }
    return render(request, 'stories.html', context)
