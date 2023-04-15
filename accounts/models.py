from django.db import models
from django.contrib.auth.models import User


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
