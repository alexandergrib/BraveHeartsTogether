from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from django.utils import timezone


class Profile(models.Model):
    user = models.ForeignKey(User, null=False,
                             blank=False, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20,
                                  help_text='First name',
                                  blank=False, null=False)
    Last_name = models.CharField(max_length=20,
                                 help_text='Last name',
                                 blank=False, null=False)
    Email = models.EmailField(max_length=20, help_text='Email',
                              blank=False, null=False)

    def __str__(self):
        return f"{self.user}"
