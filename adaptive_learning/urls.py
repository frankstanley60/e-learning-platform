# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/', views.recommend_items, name='recommendations'),
    path('adaptive-learning/', views.adaptive_learning, name='adaptive_learning'),
]
