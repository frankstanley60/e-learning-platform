from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProgress

@receiver(post_save, sender=User)
def create_user_progress(sender, instance, created, **kwargs):
    if created:
        # Check if UserProgress already exists for the User
        if not hasattr(instance, 'userprogress'):
            UserProgress.objects.create(user=instance)
