#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Content, Exercise, Question, Choice, StudentResponse, StudentExerciseCompletion

admin.site.register(Recommendation)
