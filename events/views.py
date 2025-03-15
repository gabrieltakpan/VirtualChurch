from django.shortcuts import render
from datetime import date
from .models import Event
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now


# Create your views here.
def live_event(request):
    live_stream = Event.objects.filter(is_live=True).first()
    return render(request, 'live_event.html', {'live_stream': live_stream})
