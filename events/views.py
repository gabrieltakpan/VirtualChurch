from django.shortcuts import render
from datetime import date
from .models import Event, EventType
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.utils import timezone
from django.db import models 
from urllib.parse import quote
from django.utils.dateformat import format 

def live_event(request):
    now = timezone.now()
    live_stream = Event.objects.filter(
        status='Active',  # Must be active
        stream_url__isnull=False,  # Must have a stream URL
    ).filter(
        # Either is_live=True OR current time is within start/end dates
        models.Q(is_live=True) | 
        models.Q(start_date__lte=now, end_date__gte=now)
    ).first()  # Get the first matching event
    
    return render(request, 'live_event.html', {'live_stream': live_stream})


def event_list(request):
    event_type_id = request.GET.get('event_type')
    
    if event_type_id:
        events = Event.objects.filter(event_type__id=event_type_id).order_by('-start_date')
    else:
        events = Event.objects.all().order_by('-start_date')

    # Add WhatsApp share URL to each event
    for event in events:
        event_url = request.build_absolute_uri(event.get_absolute_url())
        formatted_date = format(event.start_date, 'F j, Y \\a\\t h:i A')
        message = (
            f"Join us for *{event.title}*!\n\n"
            f"📅 *When:* {formatted_date}\n"
            f"🔗 Details: {event_url}"
        )
        event.whatsapp_share_url = f"https://wa.me/?text={quote(message)}"

    # For dropdown list
    event_types = EventType.objects.all()

    return render(request, 'event_list.html', {
        'events': events,
        'event_types': event_types,
        'selected_event_type': int(event_type_id) if event_type_id else None
    })




def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    event_url = request.build_absolute_uri(event.get_absolute_url())
    formatted_date = format(event.start_date, 'F j, Y \\a\\t h:i A')

    message = (
        f"Join us for *{event.title}*!\n\n"
        f"📅 *When:* {formatted_date}\n"
        f"🔗 *Link to Join:* {event_url}"
    )

    whatsapp_share_url = f"https://wa.me/?text={quote(message)}"

    return render(request, 'event_details.html', {
        'event': event,
        'whatsapp_share_url': whatsapp_share_url
    })
