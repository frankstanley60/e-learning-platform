# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

<<<<<<< HEAD
class CustomUserCreationForm (UserCreationForm):
    email = forms.EmailField(required=True)
=======

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
>>>>>>> ea19d24fb0863fb2f3a38818a1609df716b7aaa9

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
<<<<<<< HEAD
        fields = ()  # Leave this empty or only include fields you want in the form
        
#   UserRegistrationForm             
=======
        fields = ['preferences']

>>>>>>> ea19d24fb0863fb2f3a38818a1609df716b7aaa9
