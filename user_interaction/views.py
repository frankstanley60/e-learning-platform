from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student, Exercise, Content, StudentResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Question



class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = '__all__'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = '__all__'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Exercise
from django.urls import reverse_lazy

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'

class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'exercise_form.html'
    fields = '__all__'
    success_url = reverse_lazy('exercise_list')

class ExerciseUpdateView(UpdateView):
    model = Exercise
    template_name = 'exercise_form.html'
    fields = '__all__'
    success_url = reverse_lazy('exercise_list')

class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'exercise_confirm_delete.html'
    success_url = reverse_lazy('exercise_list')
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Content
from django.urls import reverse_lazy

class ContentListView(ListView):
    model = Content
    template_name = 'content_list.html'
    context_object_name = 'contents'

class ContentCreateView(CreateView):
    model = Content
    template_name = 'content_form.html'
    fields = '__all__'
    success_url = reverse_lazy('content_list')

class ContentUpdateView(UpdateView):
    model = Content
    template_name = 'content_form.html'
    fields = '__all__'
    success_url = reverse_lazy('content_list')

class ContentDeleteView(DeleteView):
    model = Content
    template_name = 'content_confirm_delete.html'
    success_url = reverse_lazy('content_list')
from django.views.generic import ListView
from .models import StudentResponse

class StudentResponseListView(ListView):
    model = StudentResponse
    template_name = 'studentresponse_list.html'
    context_object_name = 'studentresponses'

from django.shortcuts import render, redirect
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm

def question_list(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_choice_id = request.POST.get('choice')
        return submit_answer(request, question_id, selected_choice_id)
    return render(request, 'question_list.html', {'questions': questions})

def submit_answer(request, question_id, selected_choice_id):
    # Retrieve the question based on the question_id
    question = get_object_or_404(Question, pk=question_id)

    # Get the selected choice from the form submission
    selected_choice = question.choice_set.get(pk=selected_choice_id)

    # Determine if the selected choice is correct
    is_correct = selected_choice.is_correct

    # Check if the user has an associated Student object
    if hasattr(request.user, 'student'):
        # Create a new StudentResponse object to store the student's response
        student_response = StudentResponse.objects.create(
            student=request.user.student,
            exercise=question.exercise,
            question=question,
            choice=selected_choice,
            is_correct=is_correct,
            # Include other relevant fields such as timestamp_TW, ucid, upid, etc.
        )
        # Redirect the student to the question list page
        return redirect('question_list')
    else:
        # If the user does not have a Student object, display an error message
        messages.error(request, 'You need to be a student to submit answers.')
        return redirect('question_list')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})

def question_update(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'question_form.html', {'form': form})

def question_delete(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    return render(request, 'question_confirm_delete.html', {'question': question})

def choice_list(request):
    choices = Choice.objects.all()
    return render(request, 'choice_list.html', {'choices': choices})

def choice_create(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('choice_list')
    else:
        form = ChoiceForm()
    return render(request, 'choice_form.html', {'form': form})

def choice_update(request, pk):
    choice = Choice.objects.get(pk=pk)
    if request.method == 'POST':
        form = ChoiceForm(request.POST, instance=choice)
        if form.is_valid():
            form.save()
            return redirect('choice_list')
    else:
        form = ChoiceForm(instance=choice)
    return render(request, 'choice_form.html', {'form': form})

def choice_delete(request, pk):
    choice = Choice.objects.get(pk=pk)
    if request.method == 'POST':
        choice.delete()
        return redirect('choice_list')
    return render(request, 'choice_confirm_delete.html', {'choice': choice})

from django.shortcuts import render, get_object_or_404
from .models import Exercise, Question

def exercise_questions(request, exercise_id):
    exercise = get_object_or_404(Exercise, ucid=exercise_id)
    questions = Question.objects.filter(exercise=exercise)
    return render(request, 'exercise_questions.html', {'exercise': exercise, 'questions': questions})
