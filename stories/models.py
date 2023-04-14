from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from userprofile.models import UserProfile


class Story(models.Model):
    """
        Stories created by user
    """
    title = models.CharField(max_length=255)
    story_text = models.TextField(blank=True)
    nickname = models.CharField(max_length=125,
                                blank=True, null=True, default='Anonymous')
    anonymous = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True,
                              upload_to='blog_media',
                              )
    username = models.ForeignKey(UserProfile, null=True, blank=True,
                                 on_delete=models.DO_NOTHING)


class StoryReactions(models.Model):
    """
        To add reactions to the stories
    """

    REACTION_CHOICES = [
        (1, '&#128512'),
        (2, '&#128513'),
        (3, '&#128518'),
        (4, '&#128517'),
        (5, '&#129315'),
        (6, '&#128579'),
        (7, '&#128521'),
        (8, '&#128522'),
        (9, '&#128519'),
        (10, '&#129392'),
        (11, '&#128525'),
        (12, '&#129321'),
        (13, '&#128536'),
        (14, '&#129322'),
        (15, '&#128529'),
        (16, '&#128530'),
        (17, '&#128556'),
        (18, '&#129319'),
        (19, '&#129327'),
        (20, '&#128560'),
        (21, '&#129324'),
        (22, '&#128128'),
        (23, '&#128570'),
        (24, '&#128076'),
        (25, '&#128075'),
        (26, '&#128077'),
        (27, '&#128074'),
        (28, '&#129460'),
        (29, '&#128064'),
        (30, '&#129461'),
        (31, '&#128170'),
    ]

    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    reaction = models.PositiveIntegerField(choices=REACTION_CHOICES,
                                           validators=[
                                               MinValueValidator(1),
                                               MaxValueValidator(31)
                                           ])
    date_posted = models.DateTimeField(auto_now_add=True)
