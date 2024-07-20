from django.urls import path
from .views import ExerciseListView, ExerciseCreateView, ExerciseUpdateView, ExerciseDeleteView
from .views import ContentListView, ContentCreateView, ContentUpdateView, ContentDeleteView
from .views import StudentResponseListView
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
from . import views
from django.urls import re_path
from .views import gpt4_response
from .views import index, gpt4_response  # Import the index view





urlpatterns = [
    path('exercises/', ExerciseListView.as_view(), name='exercise_list'),
    path('exercises/create/', ExerciseCreateView.as_view(), name='exercise_create'),
    path('exercises/<pk>/update/', ExerciseUpdateView.as_view(), name='exercise_update'),
    path('exercises/<pk>/delete/', ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('contents/', ContentListView.as_view(), name='content_list'),
    path('contents/create/', ContentCreateView.as_view(), name='content_create'),
    path('contents/<pk>/update/', ContentUpdateView.as_view(), name='content_update'),
    path('contents/<pk>/delete/', ContentDeleteView.as_view(), name='content_delete'),
    path('studentresponses/', StudentResponseListView.as_view(), name='studentresponse_list'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<uuid:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<uuid:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/create/', views.question_create, name='question_create'),
    path('questions/<int:pk>/update/', views.question_update, name='question_update'),
    path('questions/<int:pk>/delete/', views.question_delete, name='question_delete'),
    path('choices/', views.choice_list, name='choice_list'),
    path('choices/create/', views.choice_create, name='choice_create'),
    path('choices/<int:pk>/update/', views.choice_update, name='choice_update'),
    path('choices/<int:pk>/delete/', views.choice_delete, name='choice_delete'),
<<<<<<< HEAD
    path('exercise/<str:exercise_id>/questions/', views.exercise_questions, name='exercise_questions'),


=======
    #path('exercise/<str:exercise_id>/questions/', views.exercise_questions, name='exercise_questions'),
    re_path(r'^exercise/(?P<exercise_id>.+)/questions/$', views.exercise_questions, name='exercise_questions'),
    path('submit_answer/<uuid:question_id>/', views.submit_answer, name='submit_answer'),
    path('user_ability/', views.estimate_user_ability, name='estimate_user_ability'),
<<<<<<< HEAD
    re_path(r'^exercise/(?P<exercise_id>.+)/answers$', views.show_answers, name='show_answers'),
    #path('exercise/<int:exercise_id>/answers/', views.show_answers, name='show_answers'),
    #path('interaction/exercise/<uuid:exercise_id>/answers/', views.show_answers, name='show_answers'),
    path('', index, name='index'),
    path('gpt4-response/', gpt4_response, name='gpt4_response'),
    
=======
>>>>>>> 47786ee06f922c2829814967e6b0ca47cee01808
>>>>>>> ea19d24fb0863fb2f3a38818a1609df716b7aaa9

    
]
