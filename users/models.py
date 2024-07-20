# users/models.py

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for user preferences, learning goals, progress data, etc.
    preferences = models.TextField(blank=True)
    learning_goals = models.TextField(blank=True)
    progress_data = models.JSONField(blank=True, null=True)

