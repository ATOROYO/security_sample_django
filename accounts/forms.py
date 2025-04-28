😁from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Form for registering new users. Inherits from Django's secure UserCreationForm.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')  # Email is our unique identifier

class CustomAuthenticationForm(AuthenticationForm):
    """
    Form for user login.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
