from django.shortcuts import render
from datetime import date
from .models import  LiveStream, Resource, Sermon
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})


def sermon_list(request):
    """ View to list all sermons """
    sermons = Sermon.objects.all()  # Fetch all sermons
    return render(request, 'sermon_list.html', {'sermons': sermons})

def sermon_detail(request, pk):
    """ View to display a single sermon with full details """
    sermon = get_object_or_404(Sermon, pk=pk)  # Get the specific sermon or return 404
    return render(request, 'sermon_detail.html', {'sermon': sermon})
