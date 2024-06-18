from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson
from .forms import LessonCreateForm, LessonEditForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#@login_required
def create_lesson(request):
    if request.method == 'POST':
        # Get the form data from the request
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')
        order_index = request.POST.get('order_index')
        difficulty_level = request.POST.get('difficulty_level')
        
        # Save the lesson to the database
        lesson = Lesson.objects.create(
            title=title,
            description=description,
            content=content,
            order_index=order_index,
            difficulty_level=difficulty_level,
            #author=request.user  # Assuming you have a logged-in user
        )
        
        # Redirect to the lesson list view
        return redirect('content_management:lesson_list')
    
    # If the request method is GET, render the create lesson form
    return render(request, 'lesson_create.html')
#@login_required
def edit_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        form = LessonEditForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('content_management:lesson_list')  # Redirect to lessons view
    else:
        form = LessonEditForm(instance=lesson)
    return render(request, 'lesson_edit.html', {'form': form, 'lesson': lesson})

#@login_required
def delete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        lesson.delete()
        return redirect('content_management:lesson_list')  # Redirect to lessons view
    return render(request, 'lesson_delete.html', {'lesson': lesson})

#@login_required
def list_lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson_list.html', {'lessons': lessons})

    

# views.py



def view_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
