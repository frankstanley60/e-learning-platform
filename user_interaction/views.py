from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student, Exercise, Content, StudentResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Question
import logging
import pytz
from django.utils import timezone
from django.http import HttpResponse
import urllib.parse
from googletrans import Translator




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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and hasattr(self.request.user, 'student'):
            student = self.request.user.student
            context['recommended_exercises'] = recommend_content(student)
        else:
            context['recommended_exercises'] = []
        return context

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

logger = logging.getLogger(__name__)

def submit_answer(request, question_id):
    logger.debug(f"submit_answer called with question_id={question_id}")

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        logger.debug(f"Selected choice ID: {selected_choice_id}")

        question = get_object_or_404(Question, pk=question_id)
        selected_choice = get_object_or_404(question.choice_set, pk=selected_choice_id)

        is_correct = selected_choice.is_correct
        logger.debug(f"Is correct choice: {is_correct}")

        if hasattr(request.user, 'student'):
            student = request.user.student
            exercise = question.exercise

            student_responses = StudentResponse.objects.filter(student=student, question=question)

            total_attempts = student_responses.count() + 1
            used_hints = student_responses.filter(used_hint_cnt__gt=0).count()
            logger.debug(f"Total attempts: {total_attempts}, Used hints: {used_hints}")

            
            current_time = timezone.now()
            rounded_time = current_time.replace(minute=15 * (current_time.minute // 15), second=0, microsecond=0)
            timestamp_TW = rounded_time.astimezone(pytz.timezone('Asia/Taipei'))
            logger.debug(f"Timestamp TW: {timestamp_TW}")
            
            if not student_responses.exists():
                problem_number = student_responses.count() + 1
            else:
                first_response = student_responses.order_by('timestamp_TW').first()
                problem_number = first_response.problem_number
            exercise_problem_repeat_session = student_responses.count() + 1
            logger.debug(f"Problem number: {problem_number}, Exercise problem repeat session: {exercise_problem_repeat_session}")

            # Calculate total time taken
            total_sec_taken = 10000
            start_time_str = request.POST.get('start_time')
            if start_time_str:
                start_time = timezone.datetime.fromisoformat(start_time_str)
            else:
                start_time = timezone.now()  # Fallback to current time if start time is missing

            end_time = timezone.now()
            total_time_taken = (end_time - start_time).total_seconds()  # Calculate duration in seconds
            logger.debug(f"Total seconds taken: {total_sec_taken}")

            # Save the student's response (add your own logic here)
            student_response = StudentResponse.objects.create(
                student=student,
                exercise=exercise,
                question=question,
                choice=selected_choice,
                timestamp_TW=timestamp_TW,
                ucid=exercise.content,
                upid=question.id,
                problem_number=problem_number,
                exercise_problem_repeat_session=exercise_problem_repeat_session,
                is_correct=is_correct,
                total_sec_taken=total_sec_taken,
                total_attempt_cnt=total_attempts,
                used_hint_cnt=used_hints
            )
            logger.debug(f"StudentResponse created: {student_response}")

        #return HttpResponse("Answer submitted")
        return redirect('show_answers', exercise_id=exercise.ucid)

    return HttpResponse("Invalid request")
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



logger = logging.getLogger(__name__)

def exercise_questions(request, exercise_id):
    # Decode the exercise_id if necessary
    exercise_id = urllib.parse.unquote(exercise_id)

    exercise = get_object_or_404(Exercise, ucid=exercise_id)
    questions = Question.objects.filter(exercise=exercise)

    # Recommend exercises based on user's ability level
    if hasattr(request.user, 'student'):
        user_ability = estimate_user_ability(request.user.student)
        recommended_exercises = recommend_content(request.user.student)
   # else:
       # user_ability = None  # or any default value
       # recommended_exercises = []  # or any default value
    
    # Logging for debugging
    logger.debug(f"Exercise ID: {exercise_id}")
    for question in questions:
        logger.debug(f"Question ID: {question.id}")
        for choice in question.choice_set.all():
            logger.debug(f"Choice ID: {choice.id}")

    return render(request, 'user_interaction/exercise_questions.html', {'exercise': exercise, 'questions': questions, 'recommended_exercises': recommended_exercises, 'user_ability': user_ability})
from django.shortcuts import render

# Create your views here.
from math import exp
from user_interaction.models import StudentResponse, ExerciseParameters  # Import your Django models

from math import log
from django.db.models import Avg

def estimate_user_ability(student):
    user_responses = StudentResponse.objects.filter(student=student)
    
    if not user_responses.exists():
        return 0

    total_ability = 0
    total_responses = 0
    
    for response in user_responses:
        try:
            item_parameters = ExerciseParameters.objects.get(exercise=response.exercise)
        except ExerciseParameters.DoesNotExist:
            continue

        # Parameters from the 3PL model
        a = item_parameters.discrimination
        b = item_parameters.difficulty
        c = item_parameters.guessing
        
        # Calculate the probability of a correct response
        theta = student.ability  # Initial estimate, you might need to update this iteratively
        P_correct = c + (1 - c) / (1 + exp(-a * (theta - b)))

        # Adjust user ability based on the response
        if response.is_correct:
            if 0 < P_correct < 1:  # Ensure P_correct is within valid range for log()
                total_ability += log(P_correct)
            else:
                # Handle cases where P_correct is outside the valid range for log()
                continue
        else:
            if 0 < (1 - P_correct) < 1:  # Ensure 1 - P_correct is within valid range for log()
                total_ability += log(1 - P_correct)
            else:
                # Handle cases where 1 - P_correct is outside the valid range for log()
                continue
        
        total_responses += 1
    
    if total_responses > 0:
        average_ability = total_ability / total_responses
    else:
        average_ability = 0
    
    return average_ability

# Update the student's ability attribute (assuming the Student model has an ability field)
def update_student_ability(student):
    student.ability = estimate_user_ability(student)
    student.save()

def recommend_content(student, num_recommendations=5):
    update_student_ability(student)
    user_ability = student.ability
    
    all_exercises = Exercise.objects.all()
    ranked_exercises = []
    
    for exercise in all_exercises:
        try:
            item_parameters = ExerciseParameters.objects.get(exercise=exercise)
        except ExerciseParameters.DoesNotExist:
            continue
        
        # Parameters from the 3PL model
        a = item_parameters.discrimination
        b = item_parameters.difficulty
        c = item_parameters.guessing
        
        try:
            # Calculate the probability of a correct response for the user's ability
            P_correct = c + (1 - c) / (1 + exp(-a * (user_ability - b)))
        except OverflowError:
            # Handle overflow error gracefully
            continue
        
        # We might rank exercises by the absolute difference between user's ability and item's difficulty
        difficulty_diff = abs(user_ability - b)
        
        ranked_exercises.append((exercise, difficulty_diff, P_correct))
    
    # Sort by difficulty difference and select top recommendations
    ranked_exercises.sort(key=lambda x: x[1])
    top_recommendations = ranked_exercises[:num_recommendations]
    
    recommended_exercises = [exercise for exercise, _, _ in top_recommendations]
    
    return recommended_exercises

# Integration in views
class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and hasattr(self.request.user, 'student'):
            student = self.request.user.student
            recommended_exercises = recommend_content(student)
            #context['recommended_exercises'] = recommend_content(student)
        else:
            recommended_exercises = []
            #context['recommended_exercises'] = []
        # Translate content_pretty_name for each recommended exercise
        translator = Translator()
        for exercise in recommended_exercises:
            exercise.content_pretty_name_translated = translator.translate(exercise.content_pretty_name, dest='en').text
        
        #exercises = Exercise.objects.all()
        #for exercise in exercises:
        #     exercise.content_pretty_name_translated = translator.translate(exercise.content_pretty_name, dest='en').text    
        context['recommended_exercises'] = recommended_exercises    
        return context


class ContentListView(ListView):
    model = Content
    template_name = 'content_list.html'
    context_object_name = 'exercises'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated and hasattr(self.request.user, 'student'):
            student = self.request.user.student
            recommended_exercises = recommend_content(student)
        else:
            recommended_exercises = []

        # Translate content_pretty_name for each recommended exercise
        translator = Translator()
        for exercise in recommended_exercises:
            exercise.content_pretty_name_translated = translator.translate(exercise.content_pretty_name, dest='en').text

        context['recommended_exercises'] = recommended_exercises
        return context
        
# Example usage:
# user = User.objects.get(pk=1)  # Assuming user is retrieved somehow
# recommended_exercises = recommend_content(user)
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, Exercise, StudentResponse, Choice

@login_required
def show_answers(request, exercise_id):
    exercise = get_object_or_404(Exercise, ucid=exercise_id)
    student = get_object_or_404(Student, user=request.user)
    responses = StudentResponse.objects.filter(student=student, exercise=exercise)
    
    answers = []
    incorrect_answers = 0

    for response in responses:
        question = response.question
        student_choice = response.choice
        correct_choice = Choice.objects.filter(question=question, is_correct=True).first()
        answers.append({
            'question': question.text,
            'student_choice': student_choice.text,
            'correct_choice': correct_choice.text,
            'is_correct': response.is_correct
        })

        if not response.is_correct:
            incorrect_answers += 1
    
    # Retrieve exercise parameters
    try:
        exercise_params = ExerciseParameters.objects.get(exercise=exercise)
        difficulty = exercise_params.difficulty
        discrimination = exercise_params.discrimination
        guessing = exercise_params.guessing

        # Calculate percentage of incorrect answers
        total_responses = responses.count()
        if total_responses > 0:
            incorrect_percentage = (incorrect_answers / total_responses) * 100
        else:
            incorrect_percentage = 0
        
        # Provide feedback based on parameters and performance
        feedback_message = ""
        if guessing > 0.5 and incorrect_percentage > 50 and total_responses > 4:
            feedback_message = "You seem to be guessing too much on this exercise. Consider revising this topic or related topics."
        elif difficulty > 0.7 and total_responses > 4:  # Example condition, adjust as per your model
            feedback_message = "This exercise is quite challenging. Focus on understanding the concepts better.try the following content in the list"

        context = {
            'exercise': exercise,
            'answers': answers,
            'feedback_message': feedback_message
        }

        return render(request, 'show_answers.html', context)

    except ExerciseParameters.DoesNotExist:
        return HttpResponse("Exercise parameters not found. Please configure them.")