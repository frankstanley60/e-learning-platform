from django.urls import path
from . import views

app_name = 'content_management'

urlpatterns = [
    path('lessons/', views.list_lessons, name='lesson_list'),
    path('lessons/create/', views.create_lesson, name='lesson_create'),
    path('lessons/<int:lesson_id>/', views.edit_lesson, name='lesson_edit'),
    path('lessons/<int:lesson_id>/delete/', views.delete_lesson, name='lesson_delete'),
    path('lessons/see/<int:lesson_id>/', views.view_lesson, name='lesson_detail'),
]
