from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    """
    A user profile for maintaining default user
    inherits from django User model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_branch = models.CharField(max_length=255)
    years_of_service = models.IntegerField()
    deployment_locations = models.CharField(max_length=255)


    def __str__(self):
        return self.user.username
