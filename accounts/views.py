from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
3
def register(request):
    """
    User registration view.
    On POST, validates the form and logs the user in.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Password is automatically hashed here
            login(request, user)  # Log the user in after successful registration
            return redirect('dashboard')  # Redirect to a protected page
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    """
    User login view.
    On POST, verifies credentials and starts a user session.
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard(request):
    """
    Dashboard view.
    Accessible only to authenticated users.
    """
    return render(request, 'accounts/dashboard.html')

def user_logout(request):
    """
    User logout view.
    Ends the user session and redirects to the login page.
    """
    logout(request)
    return redirect('login')
  
def home(request):
    return render(request, 'home.html')
