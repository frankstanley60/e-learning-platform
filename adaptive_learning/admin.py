from django.contrib import admin

# Register your models here.
from .models import LearningItem, UserProgress
admin.site.register(LearningItem)
admin.site.register(UserProgress)