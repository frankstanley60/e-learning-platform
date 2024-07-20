from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('home/', views.home, name='home'),
]
