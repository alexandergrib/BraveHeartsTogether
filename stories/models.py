from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from accounts.models import Profile
from django.contrib.auth.models import User


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
    username = models.ForeignKey(Profile, null=True, blank=True,
                                 on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)

