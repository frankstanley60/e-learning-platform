from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

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

class Exercise(models.Model):
    ucid = models.CharField(max_length=100, primary_key=True)
    content_pretty_name = models.CharField(max_length=100)
    content_kind = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20, choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Unset', 'Unset')])
    subject = models.CharField(max_length=100)
    learning_stage = models.CharField(max_length=20, choices=[('Elementary', 'Elementary'), ('Junior', 'Junior'), ('Senior', 'Senior')])
    level1_id = models.CharField(max_length=100)
    level2_id = models.CharField(max_length=100)
    level3_id = models.CharField(max_length=100)
    level4_id = models.CharField(max_length=100)

class Content(models.Model):
    ucid = models.CharField(max_length=100, primary_key=True)
    content_pretty_name = models.CharField(max_length=100)
    content_kind = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20, choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Unset', 'Unset')])
    subject = models.CharField(max_length=100)
    learning_stage = models.CharField(max_length=20, choices=[('Elementary', 'Elementary'), ('Junior', 'Junior'), ('Senior', 'Senior')])
    level1_id = models.CharField(max_length=100)
    level2_id = models.CharField(max_length=100)
    level3_id = models.CharField(max_length=100)
    level4_id = models.CharField(max_length=100)

class Question(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    text = models.TextField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

class StudentResponse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default='')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default='')
    timestamp_TW = models.DateTimeField(default=timezone.now)
    ucid = models.CharField(max_length=100)
    upid = models.IntegerField(default=uuid.uuid4)
    problem_number = models.IntegerField(default=1)
    exercise_problem_re = models.IntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    total_sec_taken = models.IntegerField(default=1)
    total_attempt_cnt = models.IntegerField(default=1)
    used_hint_cnt = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    def compare_with_correct_choice(self):
        """
        Compare the chosen choice with the correct choice for the question.
        Set is_correct field based on the comparison result.
        """
        # Get the correct choice for the question associated with this response
        correct_choice = self.choice.question.choice_set.filter(is_correct=True).first()

        # Compare the chosen choice with the correct choice
        self.is_correct = self.choice == correct_choice

        # Save the updated instance
        self.save()

    def check_exercise_completion(self):
        """
        Check if the associated exercise is completed based on the student's responses.
        """
        answered_questions_count = StudentResponse.objects.filter(student=self.student, exercise=self.exercise).count()
        total_questions_count = self.exercise.question_set.count()
        if answered_questions_count == total_questions_count:
           self.exercise.completed = True
           self.exercise.save()
        

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically check exercise completion
        when a new StudentResponse is created.
        """
        super().save(*args, **kwargs)
        # Check exercise completion
        self.check_exercise_completion()    
