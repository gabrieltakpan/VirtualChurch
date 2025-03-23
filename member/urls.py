from django.urls import path
from . import views  # Import the custom views

urlpatterns = [
    # Other URLs in your app...
    path('logout/', views.custom_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'), # URL for the login page
]
