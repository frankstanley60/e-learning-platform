from django import forms
from .models import Student, Exercise, Content, StudentResponse
from .models import Question, Choice

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['uuid', 'gender', 'points', 'badges_cnt', 'first_login_date_TW', 'user_grade', 'user_city', 'has_teacher_cnt', 'is_self_coach', 'has_student_cnt']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['ucid', 'content_pretty_name', 'content_kind', 'difficulty', 'subject', 'learning_stage', 'level1_id', 'level2_id', 'level3_id', 'level4_id']

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['ucid', 'content_pretty_name', 'content_kind', 'difficulty', 'subject', 'learning_stage', 'level1_id', 'level2_id', 'level3_id', 'level4_id']

class StudentResponseForm(forms.ModelForm):
    class Meta:
        model = StudentResponse
        fields = ['student', 'exercise', 'timestamp_TW', 'ucid', 'upid', 'problem_number', 'exercise_problem_re', 'is_correct', 'total_sec_taken', 'total_attempt_cnt', 'used_hint_cnt']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['exercise', 'text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'text', 'is_correct']