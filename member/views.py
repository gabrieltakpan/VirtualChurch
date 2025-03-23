from django.contrib.auth import logout, authenticate, login # Add this import
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Family, FamilyMember


# Optional custom logout view (if you want extra functionality)
def custom_logout(request):
    """Logs out the user and refreshes the current page."""
    logout(request)  # Logs out the user
    # Fallback to a safe page (e.g., home page) if no referer is available
    fallback_url = '/'
    referer = request.META.get('HTTP_REFERER', fallback_url)
    return redirect(referer)

def user_login(request):
    """
    Handles user login with username and password.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page (e.g., dashboard or home)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('index')  # Replace 'home' with your success URL
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # You can redirect to the login page or home page
            return redirect('index')  # Redirect to the login page
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': user_form})
