from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/', views.profile_view, name='profile')
]
