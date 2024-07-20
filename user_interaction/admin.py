#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Content, Exercise, Question, Choice, StudentResponse, StudentExerciseCompletion

admin.site.register(Student)
admin.site.register(Content)
admin.site.register(Exercise)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(StudentResponse)
admin.site.register(StudentExerciseCompletion)
