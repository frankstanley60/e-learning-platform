# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from user_interaction.models import Student
from django.shortcuts import redirect
from django.urls import reverse



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile instance and set default values for the extra fields
            profile = UserProfile.objects.create(
                user=user,
                preferences="Default preferences",  # Set default or blank
                learning_goals="Default learning goals",  # Set default or blank
                progress_data={}  # Set default or blank
            )
            student = Student.objects.create(user=user)
            
            print("User profile created and associated with user:", profile)
            return redirect(reverse('login'))  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/registration_form.html', {
        'registration_form': form,
    })
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('exercise_list'))  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login_form.html', {'login_form':form})



@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'users/edit_profile_form.html', {'edit_profile_form': form})



def profile_view(request):
    # Retrieve the user's profile data
    user_profile = UserProfile.objects.get(user=request.user)
    
    # Pass the user_profile data to the template
    return render(request, 'users/profile.html', {'user_profile': user_profile})
    
def home(request):
    return render(request, 'home.html')
