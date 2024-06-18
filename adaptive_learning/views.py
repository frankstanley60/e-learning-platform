# views.py

from django.shortcuts import render
from .models import LearningItem, UserProgress
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def recommend_items(request):
    user_progress = UserProgress.objects.get(user=request.user)
    proficiency_level = user_progress.proficiency_level
    recommended_items = LearningItem.objects.filter(level__lte=proficiency_level)[:5]
    return redirect(reverse('content_management:lesson_list'))
    #return render(request, 'recommendations.html', {'recommended_items': recommended_items})

# views.py (continued)

def adaptive_learning(request):
    user_progress = UserProgress.objects.get(user=request.user)
    proficiency_level = user_progress.proficiency_level
    next_item = LearningItem.objects.filter(level__lte=proficiency_level).first()
    return redirect(reverse('content_list'))
    #return render(request, 'adaptive_learning.html', {'next_item': next_item})

