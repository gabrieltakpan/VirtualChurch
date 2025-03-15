# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Add the path for the live_event view
    path('livestream/', views.live_event, name='live_event'),
]
