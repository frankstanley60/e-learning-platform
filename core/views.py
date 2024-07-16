from django.shortcuts import render
from content_management.models import Lesson

def dashboard(request):
    lessons = Lesson.objects.all()  # Query the lessons
    return render(request, 'core/dashboard.html', {'lessons': lessons})
    
