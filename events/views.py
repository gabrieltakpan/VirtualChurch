from django.shortcuts import render
from datetime import date
from .models import Event
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now


# Create your views here.
def live_event(request):
    live_stream = Event.objects.filter(is_live=True).first()
    return render(request, 'live_event.html', {'live_stream': live_stream})


def event_list(request):
    events = Event.objects.all().order_by('-start_date')  # Fetch all events and order by start date (newest first)
    return render(request, 'event_list.html', {'events': events})

def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch a specific event by its ID or return a 404
    return render(request, 'event_details.html', {'event': event})