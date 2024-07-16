from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
import pandas as pd
from django.db import migrations, transaction
from django.db.models import F

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gender = models.CharField(max_length=20, choices=[('male', 'Male'), ('female', 'Female'), ('unspecified', 'Unspecified'), ('null', 'Null')])
    points = models.IntegerField(default=0)
    badges_cnt = models.IntegerField(default=1)
    first_login_date_TW = models.DateTimeField(null=True)
    user_grade = models.IntegerField(default=1)
    user_city = models.CharField(max_length=100, default='')
    has_teacher_cnt = models.IntegerField(default=1)
    is_self_coach = models.BooleanField(default=False)
    has_student_cnt = models.IntegerField(default=1)
    ability = models.FloatField(default=0)

class Content(models.Model):
    ucid = models.CharField(max_length=100, primary_key=True)
    content_pretty_name = models.CharField(max_length=100)
    content_kind = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20, choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Unset', 'Unset')])
    #difficulty = models.FloatField(default=0.2)  # Difficulty parameter from the 3PL model
    discrimination = models.FloatField(default=0.2)  # Discrimination parameter from the 3PL model
    guessing = models.FloatField(default=0.1)  # Guessing parameter from the 3PL model
    subject = models.CharField(max_length=100)
    learning_stage = models.CharField(max_length=20, choices=[('Elementary', 'Elementary'), ('Junior', 'Junior'), ('Senior', 'Senior')])
    level1_id = models.CharField(max_length=100)
    level2_id = models.CharField(max_length=100)
    level3_id = models.CharField(max_length=100)
    level4_id = models.CharField(max_length=100)

    def __str__(self):
        return self.content_pretty_name

class Exercise(models.Model):
    ucid = models.CharField(primary_key=True, default=1, editable=True, max_length=100)
    content_pretty_name = models.CharField(max_length=100)
    content_kind = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20, choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Unset', 'Unset')])
   # difficulty = models.FloatField(default=0.1)  # Difficulty parameter from the 3PL model
    discrimination = models.FloatField(default=0.1)  # Discrimination parameter from the 3PL model
    guessing = models.FloatField(default=0.1)  # Guessing parameter from the 3PL model
    subject = models.CharField(max_length=100)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, null=True)
    learning_stage = models.CharField(max_length=20, choices=[('Elementary', 'Elementary'), ('Junior', 'Junior'), ('Senior', 'Senior')])
    level1_id = models.CharField(max_length=100)
    level2_id = models.CharField(max_length=100)
    level3_id = models.CharField(max_length=100)
    level4_id = models.CharField(max_length=100)

    def __str__(self):
        return self.content_pretty_name



class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    text = models.TextField()

    
    def __str__(self):
        return f"Question{self.text[:50]}..."
class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

class StudentResponse(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='student_responses')
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)
    timestamp_TW = models.DateTimeField(default=timezone.now)
    ucid = models.ForeignKey(Content, on_delete=models.CASCADE, null=True) 
    upid = models.UUIDField(default=uuid.uuid4, editable=True)
    problem_number = models.IntegerField(default=1)
    exercise_problem_repeat_session = models.IntegerField(default=1)  # New field added
    is_correct = models.BooleanField(default=False)
    total_sec_taken = models.IntegerField(default=0)
    total_attempt_cnt = models.IntegerField(default=0)
    used_hint_cnt = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.student} - {self.question} - {self.choice} - {self.timestamp_TW}'

    def compare_with_correct_choice(self):
        correct_choice = self.choice.question.choice_set.filter(is_correct=True).first()
        self.is_correct = self.choice == correct_choice
        self.save()

    def check_exercise_completion(self):
        answered_questions_count = StudentResponse.objects.filter(student=self.student, exercise=self.exercise).count()
        total_questions_count = self.exercise.question_set.count()
        if answered_questions_count == total_questions_count:
            StudentExerciseCompletion.objects.create(student=self.student, exercise=self.exercise, completed=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.check_exercise_completion()

class StudentExerciseCompletion(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(default=timezone.now)

class ExerciseParameters(models.Model):
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE, primary_key=True)
    difficulty = models.FloatField()  # Parameter 'a'
    discrimination = models.FloatField()  # Parameter 'b'
    guessing = models.FloatField()  # Parameter 'c'

def update_question_numbers(apps, schema_editor):
    Question = apps.get_model('user_interaction', 'Question')
    Exercise = apps.get_model('user_interaction', 'Exercise')

    for exercise in Exercise.objects.all():
        questions = Question.objects.filter(exercise=exercise).order_by('id')
        for i, question in enumerate(questions, start=1):
            question.question_number = i
            question.save()

class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', 'previous_migration_file'),
    ]

    operations = [
        migrations.RunPython(update_question_numbers),
    ]
