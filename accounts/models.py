from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, null=False,
                                on_delete=models.CASCADE)
    First_name = models.CharField(max_length=25,
                                  help_text='First name',
                                  blank=False, null=False)
    Last_name = models.CharField(max_length=25,
                                 help_text='Last name',
                                 blank=False, null=False)
    Email = models.EmailField(max_length=20, help_text='Email',
                              blank=False, null=False)
    About = models.CharField(max_length=25,
                                 help_text='About',
                                 blank=True, null=True)
    def __str__(self):
        return f"{self.user}"

#
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created:
#         Profile.objects.create(user=instance)
#     # Existing users: just save the profile
#     instance.userprofile.save()
