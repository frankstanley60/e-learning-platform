# models.py

from django.db import models
from django.contrib.auth.models import User

class LearningItem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    content_type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    question = models.TextField()

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proficiency_level = models.FloatField(default=0.0)  # Initial proficiency level
