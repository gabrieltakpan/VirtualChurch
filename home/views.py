from django.shortcuts import render
from datetime import date
from .models import  Resource, ResourceType, Sermon
from events.models import Event
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def about(request):
    return render(request, 'about.html')


def resources(request):
    type_id = request.GET.get('type')
    
    if type_id:
        resources = Resource.objects.filter(resource_type__id=type_id)
    else:
        resources = Resource.objects.all()

    resource_types = ResourceType.objects.all()

    return render(request, 'resources.html', {
        'resources': resources,
        'resource_types': resource_types,
        'selected_type': int(type_id) if type_id else None
    })



def sermon_list(request):
    """ View to list all sermons """
    sermons = Sermon.objects.all()  # Fetch all sermons
    return render(request, 'sermon_list.html', {'sermons': sermons})

def sermon_detail(request, pk):
    """ View to display a single sermon with full details """
    sermon = get_object_or_404(Sermon, pk=pk)  # Get the specific sermon or return 404
    return render(request, 'sermon_detail.html', {'sermon': sermon})

def donate(request):
    return render(request, 'donate.html')
